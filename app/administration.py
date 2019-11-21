from django.shortcuts import render

from app.helpers import GENDERS, ok_json
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
        'categories': Category.objects.all(),
        'pid': 0
    }
    if request.method == 'POST':
        payload = request.POST
        print(payload)
        return ok_json(data={'message': 'Correct'})

    return render(request, 'administration/product.html', data)


def edit_product(request, product_id):
    data = {
        'title': 'Sabadiaz Jewelry Admin - Edit Product',
        'option': 'admin_edit_product',
        'user': request.user,
        'genders': GENDERS,
        'categories': Category.objects.all(),
        'pid': product_id
    }
    return render(request, 'administration/product.html', data)