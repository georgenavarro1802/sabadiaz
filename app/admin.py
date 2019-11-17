from django.contrib import admin

from app.models import Category, Product, WishList


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    ordering = ('name', )
    search_fields = ('name', )


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'name', 'description', 'price', 'stock', 'is_new')
    ordering = ('category', 'name')
    search_fields = ('category__name', 'name', 'description')
    list_filter = ('is_new', 'gender')


admin.site.register(Product, ProductAdmin)


class WishListAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'created_at')
    ordering = ('-created_at', )
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'product__name', 'product__description')


admin.site.register(WishList, WishListAdmin)
