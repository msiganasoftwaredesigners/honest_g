from django.contrib import admin
from .models import Image
from msigana_ecommerce.admin_site import admin_site


class ImageAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "image")
    search_fields = ("name",)
admin_site.register(Image, ImageAdmin)
