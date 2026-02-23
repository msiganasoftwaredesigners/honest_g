from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver


class BackgroundSlide(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='slides/')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.image:
            img = Image.open(self.image)

            # Convert to RGB
            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")

            # ✅ FIXED for new Pillow
            try:
                resample = Image.Resampling.LANCZOS
            except AttributeError:
                resample = Image.ANTIALIAS

            # Resize
            max_size = (1920, 1080)
            img.thumbnail(max_size, resample)

            # Compress to target KB
            target_size_kb = 500
            target_size_bytes = target_size_kb * 1024

            output = BytesIO()
            quality = 85

            while True:
                img.save(output, format="JPEG", quality=quality)
                if output.tell() <= target_size_bytes or quality <= 10:
                    break
                quality -= 5
                output.seek(0)
                output.truncate()

            output.seek(0)
            self.image = ContentFile(output.read(), self.image.name)

        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        try:
            self.image.delete(save=False)
        except Exception:
            pass
        super().delete(*args, **kwargs)


# ✅ Signals
@receiver(post_delete, sender=BackgroundSlide)
def delete_slide_image(sender, instance, **kwargs):
    instance.image.delete(save=False)


@receiver(pre_save, sender=BackgroundSlide)
def delete_old_slide_image(sender, instance, **kwargs):
    if instance.pk:
        old_image = BackgroundSlide.objects.get(pk=instance.pk).image
        if old_image != instance.image:
            old_image.delete(save=False)