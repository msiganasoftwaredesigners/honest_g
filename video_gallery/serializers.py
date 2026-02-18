from rest_framework import serializers
from .models import Video

class VideoSerializer(serializers.ModelSerializer):
    youtube_embed = serializers.SerializerMethodField()  # Add this field

    class Meta:
        model = Video
        fields = ['title', 'youtube_url', 'youtube_embed']

    def get_youtube_embed(self, obj):
        return obj.embed_url()  # Call the embed_url method from the Video model
