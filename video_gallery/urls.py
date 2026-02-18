from django.urls import path
from .views import video_list, video_gallery

urlpatterns = [
    path('', video_gallery, name="video-gallery"),
    path('api/videos/', video_list, name="video-list"),
]
