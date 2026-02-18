from django.shortcuts import render
from slideshow.models import BackgroundSlide
from store.models import Product
from users.forms import ProfileForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.http import HttpResponse
from django.conf import settings
from main_video.models import Video
import os
def home(request):
    #products = Product.objects.filter(product_is_available=True).order_by('-product_modified_date', '-product_created_date')
    products = Product.objects.filter(product_is_available=True).order_by('-product_modified_date', '-product_created_date')
    # for pro in products:
    #     print(f" valueeeeeeeeeeeee: {pro.product_modified_date}, {pro.product_created_date}, {pro.product_name}")
    video = Video.objects.first()  # Get the first available video

    # Get the embedded URLs for different device types
    mobile_video_url = video.get_embedded_url('mobile')
    tablet_video_url = video.get_embedded_url('tablet')
    desktop_video_url = video.get_embedded_url('desktop')
    slides = BackgroundSlide.objects.filter(is_active=True)

    context = {
        'products': products,
        'video': video,  # Add video to the context for reference if needed
        'mobile_video_url': mobile_video_url,
        'tablet_video_url': tablet_video_url,
        'desktop_video_url': desktop_video_url,
        'slides': slides
    }

    return render(request, 'index.html', context)


def privacy_policy(request):
    return render(request, 'privacy-policy.html')

def hours_location(request):
    return render(request, 'hours-location.html' )
def happenings(request):
    return render(request, 'happenings.html')
def new_arrivals(request):
    products = Product.objects.all().filter(product_is_available=True)
    context = {
        'products': products
    }
    return render(request, 'new-arrivals.html', context)

def online_order(request):
    products = Product.objects.all().filter(product_is_available=True)
    context = {
        'products': products
    }
    return render(request, 'online_order.html', context)


@login_required
def update_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save()
            return JsonResponse({
                'first_name': user.first_name,
                'last_name': user.last_name,
                'phone_number': user.phone_number,
                'address': user.address,
            })
    else:
        form = ProfileForm(instance=request.user)
    orders = request.user.order_set.order_by('-order_date')[:6]
    liked_products = request.user.liked_products.all()

    return render(request, 'profile.html', {'form': form, 'orders': orders, 'liked_products': liked_products})
