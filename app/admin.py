from django.contrib import admin

from app.models import Category, Product, WishList, Slide, Company, Testimonial, Material, Gender, Review, Contact


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    ordering = ('name', )
    search_fields = ('name', )


admin.site.register(Category, CategoryAdmin)


class MaterialAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    ordering = ('name', )
    search_fields = ('name', )


admin.site.register(Material, MaterialAdmin)


class GenderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    ordering = ('name', )
    search_fields = ('name', )


admin.site.register(Gender, GenderAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'material', 'title', 'description', 'created_at',
                    'price', 'v_price', 'stock', 'is_new', 'is_featured', 'is_bestseller')
    ordering = ('-created_at', )
    search_fields = ('category__name', 'material__name', 'title', 'description')
    list_filter = ('gender', 'material', 'category', 'is_new', 'is_featured', 'is_bestseller')


admin.site.register(Product, ProductAdmin)


class WishListAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'created_at')
    ordering = ('-created_at', )
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'product__title', 'product__description')


admin.site.register(WishList, WishListAdmin)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'user', 'product', 'rating', 'review')
    ordering = ('-created_at', )
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'product__title', 'product__description')
    list_filter = ('rating', )


admin.site.register(Review, ReviewAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'name', 'email', 'phone', 'subject', 'message')
    ordering = ('-created_at', )
    search_fields = ('name', 'email', 'subject')


admin.site.register(Contact, ContactAdmin)


# Company
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'address', 'email', 'phone', 'logo',
                    'facebook', 'twitter', 'instagram', 'youtube')
    search_fields = ('name', 'description', 'email')


admin.site.register(Company, CompanyAdmin)


# Slides
class SlideAdmin(admin.ModelAdmin):
    list_display = ('text1', 'text2', 'description', 'image')
    search_fields = ('text1', 'text2', 'description')


admin.site.register(Slide, SlideAdmin)


# Testimonials
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'testimonial', 'avatar')
    search_fields = ('name', 'testimonial')


admin.site.register(Testimonial, TestimonialAdmin)
