from django.urls import path
from .views import ImageListView, gallery_view

urlpatterns = [
    path("", gallery_view, name="gallery"),
    path("api/images/", ImageListView.as_view(), name="image-list"),
]
