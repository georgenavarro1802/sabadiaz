from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from app.models import Category, Product, WishList, Slide, Company, Testimonial, Material, Gender, Review, Contact


class CategoryAdmin(TranslationAdmin):
    list_display = ('id', 'name_en', 'name_es')
    search_fields = ('name_en', 'name_es',)
    ordering = ('id', )


admin.site.register(Category, CategoryAdmin)


class MaterialAdmin(TranslationAdmin):
    list_display = ('id', 'name_en', 'name_es')
    search_fields = ('name_en', 'name_es',)
    ordering = ('id',)


admin.site.register(Material, MaterialAdmin)


class GenderAdmin(TranslationAdmin):
    list_display = ('id', 'name_en', 'name_es')
    search_fields = ('name_en', 'name_es',)
    ordering = ('id',)


admin.site.register(Gender, GenderAdmin)


class ProductAdmin(TranslationAdmin):
    list_display = ('id', 'category', 'material', 'gender', 'title_en', 'title_es', 'description_en', 'description_es',
                    'created_at', 'price', 'v_price', 'stock', 'is_new', 'is_featured', 'is_bestseller')
    ordering = ('-created_at', )
    search_fields = ('category__name', 'material__name', 'title_en', 'title_es', 'description_en', 'description_es')
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
    list_display = ('name', 'description_en', 'description_es', 'address', 'email', 'phone', 'logo',
                    'facebook', 'twitter', 'instagram', 'youtube')
    search_fields = ('name', 'description_en', 'description_es', 'email')


admin.site.register(Company, CompanyAdmin)


# Slides
class SlideAdmin(admin.ModelAdmin):
    list_display = ('id', 'text1_en', 'text1_es', 'text2_en', 'text2_es', 'description_en', 'description_es', 'image')
    search_fields = ('text1_en', 'text1_es', 'text2_en', 'text2_es', 'description_en', 'description_es')
    ordering = ('id', )


admin.site.register(Slide, SlideAdmin)


# Testimonials
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'testimonial_en', 'testimonial_es', 'avatar')
    search_fields = ('name', 'testimonial_en', 'testimonial_es')


admin.site.register(Testimonial, TestimonialAdmin)
