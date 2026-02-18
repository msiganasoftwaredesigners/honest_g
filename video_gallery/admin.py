from django.contrib import admin
from .models import Video
from msigana_ecommerce.admin_site import admin_site


class   VideoAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "youtube_url", "uploaded_at")
    search_fields = ("name",)
admin_site.register(Video, VideoAdmin)
