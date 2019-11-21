from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from app import views, administration
from sabadiaz.settings import DEBUG, MEDIA_URL, MEDIA_ROOT, STATIC_URL, STATIC_ROOT

urlpatterns = [

    # admin
    path('admin/', admin.site.urls),

    # index
    path('', views.index, name='index'),

    # Login
    path('login', views.login_user, name='login'),

    # Logout
    path('logout', views.logout_user, name='logout'),

    # Register
    path('register', views.register, name='register'),

    # My Account
    path('account', views.account, name='account'),

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

    # Administration Panel
    path('administration/products', administration.products, name='admin_products'),
    path('administration/products/create', administration.create_product, name='admin_create_product'),
    path('administration/products/<int:product_id>/edit', administration.edit_product, name='admin_edit_product'),


]


if DEBUG:
    urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
