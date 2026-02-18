from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from .models import Image
from .serializers import ImageSerializer
from django.shortcuts import render

class ImagePagination(PageNumberPagination):
    page_size = 6

class ImageListView(ListAPIView):
    queryset = Image.objects.all().order_by('-created_at')
    serializer_class = ImageSerializer
    pagination_class = ImagePagination

def gallery_view(request):
    return render(request, "gallery.html")