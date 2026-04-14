from django.db import models
from django.urls import reverse

# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    category_slug = models.SlugField(max_length=100, unique=100)
    description = models.TextField(max_length=40, blank=True)
    category_image = models.ImageField(upload_to='images/categories', blank=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('products_by_category', args=[self.category_slug])

    def __str__(self):
        return self.category_name
    
    def save(self, *args, **kwargs):
        try:
            # is the object in the database yet?
            this = Category.objects.get(id=self.id)
            if this.category_image != self.category_image:
                this.category_image.delete(save=False)
        except: pass # when new photo then we do nothing, normal case
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # Delete the actual image file
        try:
            if os.path.isfile(self.category_image.path):
                os.remove(self.category_image.path)
        except PermissionError:
            print("Permission denied: Unable to delete the image file.")
        except Exception as e:
            print(f"Unexpected error occurred while deleting the image file: {e}")
        super().delete(*args, **kwargs)


class ParkingSpace(models.Model):
    parking_name = models.CharField(max_length=50, unique=True,default='No Parking Space')
    parking_slug = models.SlugField(max_length=100, unique=100)

    class Meta:
        verbose_name = 'parking space'
        verbose_name_plural = 'parking spaces'
    
    def __str__(self):
        return self.parking_name
# condition of home class
class Condition(models.Model):
    condition_name = models.CharField(max_length=50, unique=True,default='No Condition')
    condition_slug = models.SlugField(max_length=100, unique=100)

    class Meta:
        verbose_name = 'condition'
        verbose_name_plural = 'conditions'
    
    def __str__(self):
        return self.condition_name
# number of bedroom class
class Bedroom(models.Model):
    bedroom_name = models.CharField(max_length=50, unique=True,default='No Bedroom')
    bedroom_slug = models.SlugField(max_length=100, unique=100)

    class Meta:
        verbose_name = 'bedroom'
        verbose_name_plural = 'bedrooms'
    
    def __str__(self):
        return self.bedroom_name
# number of bathroom class
class Bathroom(models.Model):
    bathroom_name = models.CharField(max_length=50, unique=True,default='No Bathroom')
    bathroom_slug = models.SlugField(max_length=100, unique=100)

    class Meta:
        verbose_name = 'bathroom'
        verbose_name_plural = 'bathrooms'
    
    def __str__(self):
        return self.bathroom_name
# number of kitchen class
class Kitchen(models.Model):
    kitchen_name = models.CharField(max_length=50, unique=True,default='No Kitchen')
    kitchen_slug = models.SlugField(max_length=100, unique=100)

    class Meta:
        verbose_name = 'kitchen'
        verbose_name_plural = 'kitchens'
    
    def __str__(self):
        return self.kitchen_name