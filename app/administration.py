from django.shortcuts import render


def products(request):
    data = {
        'title': 'Sabadiaz Jewelry Admin - All Products',
        'option': 'admin_products',
        'user': request.user,
        'lista': [x for x in range(20)]
    }
    return render(request, 'administration/products.html', data)