from django.shortcuts import render


def products(request):
    data = {
        'title': 'Sabadiaz Jewelry Admin - All Products',
        'option': 'products',
        'user': request.user
    }
    return render(request, 'administration/products.html', data)