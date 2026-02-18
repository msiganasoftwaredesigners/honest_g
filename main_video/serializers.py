# main_video/serializers.py
from rest_framework import serializers
from .models import Video

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['mobile_video_url', 'tablet_video_url', 'desktop_video_url']
