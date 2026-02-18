#store/context_processors.py
from django.utils import timezone
from datetime import timedelta
from django.core.cache import cache
from .models import Product
from django.db.models import Count, Q
from django.core.exceptions import ObjectDoesNotExist
import logging


def most_liked_products(request):
    try:
        # Try to fetch the most liked products from cache
        most_liked_products = cache.get('most_liked_products')

        # If the most liked products are not in cache or cache is stale, recalculate them
        if most_liked_products is None:
            # Get the date 90 days ago
            ninety_days_ago = timezone.now() - timedelta(days=90)

            # Get the most liked products in the last 90 days
            most_liked_products = Product.objects.filter(
                product_modified_date__gte=ninety_days_ago
            ).annotate(
                likes_count=Count('likes')
            ).order_by('-likes_count')[:8]

            # Store the most liked products in cache for 3 days
            cache.set('most_liked_products', most_liked_products, 60*60*0)
        else:
            # Check if the products in cache still exist in the database
            updated_products = []
            for product in most_liked_products:
                try:
                    Product.objects.get(id=product.id)
                    updated_products.append(product)
                except ObjectDoesNotExist:
                    pass  # Product no longer exists, skip

            most_liked_products = updated_products

    except Exception as e:
        # Handle exceptions gracefully, log the error, and provide a fallback response
        logging.error(f"Error fetching most liked products: {e}")
        most_liked_products = []

    return {'most_liked_products': most_liked_products}



def unique_locations(request):
    locations = (
        Product.objects.exclude(product_location__isnull=True)
        .exclude(product_location__exact='')
        .values_list('product_location', flat=True)
        .distinct()
    )
    return {'unique_locations': sorted(set(locations))}



def categorized_locations(request):
    from .models import Product

    category_map = {
        'Office Rent': 'Office Rent',
        'Rent Your Home': 'Rent Your Home',
        'Buy Your House': 'Buy Your House',
    }

    categorized = {}
    for key, category in category_map.items():
        locations = (
            Product.objects.filter(category__category_name__iexact=category)
            .exclude(product_location__isnull=True)
            .exclude(product_location__exact='')
            .values_list('product_location', flat=True)
            .distinct()
        )
        categorized[key] = sorted(set(locations))

    return {'categorized_locations': categorized}



from .models import SitesShowFooter

def footer_links(request):
    links = SitesShowFooter.objects.all()

    # Optional: use first one with video
    first_site = links.first()
    if first_site:
        mobile_video_url = first_site.get_embedded_url('mobile')
        tablet_video_url = first_site.get_embedded_url('tablet')
        desktop_video_url = first_site.get_embedded_url('desktop')
    else:
        mobile_video_url = tablet_video_url = desktop_video_url = ""

    return {
        'footer_sites_links': links,
        'mobile_video_url': mobile_video_url,
        'tablet_video_url': tablet_video_url,
        'desktop_video_url': desktop_video_url,
    }
