from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from app import views, wishlist, shop
from app.administration import products, slides, company, testimonials
from sabadiaz.settings import MEDIA_URL, MEDIA_ROOT, STATIC_URL, STATIC_ROOT

urlpatterns = [

    # admin
    path('admin/', admin.site.urls),

    # set languages
    path('i18n/', include('django.conf.urls.i18n')),

    # Administration - Products
    path('administration/products', products.view, name='admin_products'),
    path('administration/products/create', products.create_product, name='admin_create_product'),
    path('administration/products/<int:product_id>/edit', products.edit_product, name='admin_edit_product'),
    path('administration/products/<int:product_id>/delete', products.delete_product, name='admin_delete_product'),
    path('administration/products/<int:product_id>/images/<int:image_id>/delete', products.delete_product_image,
         name='admin_delete_product_image'),
    path('administration/products/<int:product_id>/images/<int:image_id>/edit', products.edit_product_image,
         name='admin_edit_product_image'),

    # Administration
    # Company
    path('administration/website/company/update', company.company_data, name='admin_website_company_data'),
    path('administration/website/company/logo', company.company_logo, name='admin_website_company_logo'),

    # Slides
    path('administration/website/slides', slides.view, name='admin_website_slides'),
    path('administration/website/slides/<int:slide_id>/update_image', slides.update_image,
         name='admin_website_slides_update_image'),

    # Testimonials
    path('administration/website/testimonials', testimonials.view, name='admin_website_testimonials'),
    path('administration/website/testimonials/<int:testimonial_id>/update_avatar', testimonials.update_avatar,
         name='admin_website_testimonials_update_avatar'),
]

urlpatterns += i18n_patterns(

    # index
    path('', views.index, name='index'),
    # path('', views.coming_soon, name='index'),

    # Login
    path('login', views.login_user, name='login'),

    # Logout
    path('logout', views.logout_user, name='logout'),

    # Register
    path('register', views.register, name='register'),

    # My Account
    path('account', views.account, name='account'),

    # About Us
    path('about', views.about, name='about'),

    # Contact Us
    path('contact', views.contact, name='contact'),

    # Wishlist
    path('wishlist', wishlist.view, name='wishlist'),
    path('wishlist/<int:product_id>/add', wishlist.add, name='wishlist_add'),
    path('wishlist/<int:item_id>/delete', wishlist.delete, name='wishlist_delete'),

    # Our Products
    path('products', shop.view, name='products'),
    path('products/<int:product_id>/details', shop.details, name='product_details'),
    path('products/<int:product_id>/reviews', shop.reviews, name='product_reviews'),

)

urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)
urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
