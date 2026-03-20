from django.db import models
from django.utils.text import slugify
from PIL import Image
from django.core.files.base import ContentFile
from io import BytesIO
from django_quill.fields import QuillField
from django.utils.html import strip_tags
import html


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = QuillField()
    image = models.ImageField(upload_to='images/posts', blank=False)
    slug = models.SlugField(max_length=200, unique=True)
    short_description = models.CharField(max_length=200, blank=True)

    def get_plain_title(self):
        return strip_tags(self.title)

    def save(self, *args, **kwargs):
        try:
            this = Post.objects.get(id=self.id)
            if this.image != self.image:
                this.image.delete(save=False)
        except Post.DoesNotExist:
             pass

        self.slug = slugify(self.title)

        if self.content:
            plain_text_content = html.unescape(strip_tags(str(self.content.html)))
            self.short_description = plain_text_content[:150]

        # Optimize image before saving
        if self.image:
            img = Image.open(self.image)

            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")

            output = BytesIO()
            img.save(output, format="JPEG", quality=75)
            output.seek(0)

            file_name = self.image.name.split('.')[0] + ".jpg"
            self.image = ContentFile(output.read(), file_name)

        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.image.delete(save=False)
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.title