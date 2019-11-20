from django.shortcuts import render

from app.models import Product


def products(request):
    data = {
        'title': 'Sabadiaz Jewelry Admin - All Products',
        'option': 'admin_all_products',
        'user': request.user,
        'lista': [x for x in range(20)],
        'products': Product.objects.all()
    }
    return render(request, 'administration/products.html', data)


def create_product(request):
    data = {
        'title': 'Sabadiaz Jewelry Admin - Create Product',
        'option': 'admin_create_product',
        'user': request.user,
    }
    return render(request, 'administration/create_product.html', data)