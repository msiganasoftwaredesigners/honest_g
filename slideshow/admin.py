from django.contrib import admin
from .models import BackgroundSlide
from msigana_ecommerce.admin_site import admin_site


class BackgroundSlideAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active')
    list_filter = ('is_active',)


admin_site.register(BackgroundSlide, BackgroundSlideAdmin)