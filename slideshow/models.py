from django.db import models

class BackgroundSlide(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='slides/')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
