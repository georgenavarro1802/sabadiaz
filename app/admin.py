from django.contrib import admin

from app.models import Category, Product, WishList, HomeSlider


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    ordering = ('name', )
    search_fields = ('name', )


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'material', 'title', 'description', 'created_at',
                    'price', 'v_price', 'stock', 'is_new', 'is_featured', 'is_bestseller', 'is_onsale')
    ordering = ('-created_at', )
    search_fields = ('category__name', 'title', 'description')
    list_filter = ('gender', 'material', 'is_new', 'is_featured', 'is_bestseller', 'is_onsale')


admin.site.register(Product, ProductAdmin)


class WishListAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'created_at')
    ordering = ('-created_at', )
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'product__title', 'product__description')


admin.site.register(WishList, WishListAdmin)


# Website HomePage
class HomeSliderAdmin(admin.ModelAdmin):
    list_display = ('text1', 'text2', 'description', 'image')
    search_fields = ('text1', 'text2', 'description')


admin.site.register(HomeSlider, HomeSliderAdmin)
