# main_video/urls.py
from django.urls import path
from .views import VideoView

urlpatterns = [
    path('api/video/', VideoView.as_view(), name='video_api'),
]
