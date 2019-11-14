from django.contrib import admin
from django.urls import path
from app import views


urlpatterns = [

    # admin
    path('admin/', admin.site.urls),

    # index
    path('', views.index, name='index'),

    # Shop
    path('shop', views.shop, name='shop'),

    # About Us
    path('about', views.about, name='about'),

    # Contact Us
    path('contact', views.contact, name='contact'),

    # Wishlist
    path('wishlist', views.wishlist, name='wishlist'),

    # Product Details
    path('products/<int:product_id>/details', views.product_details, name='product_details'),

]
