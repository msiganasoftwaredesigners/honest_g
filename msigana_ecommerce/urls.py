from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from msigana_ecommerce.admin_site import admin_site
from django.views.generic import TemplateView
from django.contrib.staticfiles.views import serve

# from django.contrib import admin

urlpatterns = [
    path('admin/', admin_site.urls),
    path('', views.home, name='home'),
    path('homes/', include('store.urls')),
    path('news/', include('blog.urls')),
    path('privacy-policy/', views.privacy_policy, name='privacy-policy'),
    path('contact-us/', include('contact.urls')),
    path('accounts/', include('allauth.urls')),
    path("accounts/profile/", views.update_profile, name="users_profiles"),
    path("gallery/", include("gallery.urls")),
    path("video-gallery/", include("video_gallery.urls")),
    path('main_video/', include('main_video.urls')),
    path('about-us/', include('team.urls')),
   

]


if settings.DEBUG:
    urlpatterns += [
        path("__reload__/", include("django_browser_reload.urls")),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #media setup

