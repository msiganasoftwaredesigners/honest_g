from django.urls import path
from . import views
from .views import finished_products_view, unfinished_products_view, new_products_view


urlpatterns = [
    path('projects/finished/', finished_products_view, name='finished_projects'),
    path('projects/unfinished/', unfinished_products_view, name='unfinished_projects'),
    path('projects/new/', new_products_view, name='new_projects'),
    path('filter_products/', views.filter_products, name='filter_products'),
    path('increment-view-count/<slug:product_slug>/', views.increment_view_count, name='increment_view_count'),
    path('rate_product/<str:product_slug>/', views.rate_product, name='rate_product'),
    path('<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),
    path('get_price_and_colors/', views.get_price_and_colors, name='get_price_and_colors'),
    path('<slug:category_slug>/', views.store, name='products_by_category'),
    path('', views.store, name='store'),
    path('search', views.search, name='search'),
    path('product/<slug:product_slug>/like/', views.like_product, name='like_product'),
    # path('location/<str:location>/', views.products_by_location, name='products_by_location'),
    path('sites/<str:category>/<str:location>/', views.products_by_location, name='products_by_location'),

]
