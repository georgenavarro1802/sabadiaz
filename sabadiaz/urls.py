from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from app import views
from app.administration import products, webite
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

    # Administration - Products
    path('administration/products', products.view, name='admin_products'),
    path('administration/products/create', products.create_product, name='admin_create_product'),
    path('administration/products/<int:product_id>/edit', products.edit_product, name='admin_edit_product'),
    path('administration/products/<int:product_id>/delete', products.delete_product, name='admin_delete_product'),
    path('administration/products/<int:product_id>/images/<int:image_id>/delete', products.delete_product_image, name='admin_delete_product_image'),
    path('administration/products/<int:product_id>/images/<int:image_id>/edit', products.edit_product_image, name='admin_edit_product_image'),

    # Administration - HomeSliders
    path('administration/website/company/update', webite.company_data, name='admin_website_company_data'),
    path('administration/website/company/logo', webite.company_logo, name='admin_website_company_logo'),
    path('administration/website/home_sliders', webite.home_sliders, name='admin_website_home_sliders'),
    path('administration/website/home_sliders/<int:hs_id>/update_image', webite.home_sliders_update_image, name='admin_website_home_sliders_update_image'),

]


if DEBUG:
    urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
