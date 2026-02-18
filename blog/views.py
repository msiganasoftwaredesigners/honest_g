from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from .models import Post
from .serializers import PostSerializer  # spelling corrected to PostSerializer
from django.shortcuts import get_object_or_404, render

# ✅ Custom pagination (optional)
class PostPagination(PageNumberPagination):
    page_size = 6  # Number of posts per page
    page_size_query_param = 'page_size'
    max_page_size = 20

# ✅ List view (for JS to consume)
class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.all().order_by('-id')  # newest first
    serializer_class = PostSerializer
    pagination_class = PostPagination

# ✅ Detail view (optional if you need it)
class PostDetailAPIView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'

def blog_page(request):
    return render(request, 'post_list.html')

def blog_post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'post_detail.html', {'post': post})