from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=255)
    youtube_url = models.URLField(unique=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def embed_url(self):
        """Extracts YouTube video ID and returns the embeddable URL."""
        if "youtube.com/watch?v=" in self.youtube_url:
            video_id = self.youtube_url.split("watch?v=")[-1].split("&")[0]
            return f"https://www.youtube.com/embed/{video_id}"
        elif "youtu.be/" in self.youtube_url:
            video_id = self.youtube_url.split("youtu.be/")[-1].split("?")[0]
            return f"https://www.youtube.com/embed/{video_id}"
        return self.youtube_url

    def __str__(self):
        return self.title
