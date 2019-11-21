from django.shortcuts import render

from app.helpers import GENDERS
from app.models import Product, Category


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
        'genders': GENDERS,
        'categories': Category.objects.all()
    }
    return render(request, 'administration/create_product.html', data)