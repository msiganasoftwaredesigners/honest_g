from django.urls import path
from . import views
from .views import PostListAPIView, PostDetailAPIView

urlpatterns = [
    path('', views.blog_page, name='blog'),  
    path('<slug:slug>/', views.blog_post_detail, name='blog_post_detail'),
    path('api/posts/', PostListAPIView.as_view(), name='post_list'),  # <-- API endpoint
    path('api/posts/<slug:slug>/', PostDetailAPIView.as_view(), name='post_detail'),
]
