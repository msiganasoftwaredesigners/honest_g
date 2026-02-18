# main_video/models.py
from django.db import models

class Video(models.Model):
    mobile_video_url = models.URLField()
    tablet_video_url = models.URLField()
    desktop_video_url = models.URLField()
    
    def __str__(self):
        return f"Video: {self.mobile_video_url} - {self.tablet_video_url} - {self.desktop_video_url}"

    def get_embedded_url(self, device_type):
        """
        Returns the YouTube embedded URL based on device type.
        """
        # Ensure the video URL is in the correct YouTube embed format
        def to_embed_url(video_url):
            if video_url:
                # Extract video ID from the URL and format it as an embed URL
                video_id = video_url.split("v=")[-1]
                return f"https://www.youtube.com/embed/{video_id}"
            return ""
        
        if device_type == 'mobile':
            return to_embed_url(self.mobile_video_url)
        elif device_type == 'tablet':
            return to_embed_url(self.tablet_video_url)
        elif device_type == 'desktop':
            return to_embed_url(self.desktop_video_url)
        return ""


