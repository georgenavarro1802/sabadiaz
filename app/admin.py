from django.contrib import admin

from app.models import Category, Product, WishList


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    ordering = ('name', )
    search_fields = ('name', )


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'title', 'description', 'price', 'v_price', 'stock', 'is_new', 'created_at')
    ordering = ('-created_at', )
    search_fields = ('category__name', 'title', 'description')
    list_filter = ('is_new', 'gender')


admin.site.register(Product, ProductAdmin)


class WishListAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'created_at')
    ordering = ('-created_at', )
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'product__title', 'product__description')


admin.site.register(WishList, WishListAdmin)
