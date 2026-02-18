# main_video/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Video
from .serializers import VideoSerializer

class VideoView(APIView):
    def get(self, request):
        video = Video.objects.first()  # Or filter to get a specific video if needed
        serializer = VideoSerializer(video)
        return Response(serializer.data)
