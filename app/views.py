from django.shortcuts import render


def index(request):
    data = {
        'title': 'Sabadiaz Jewelry - Welcome',
        'option': 'index'
    }
    return render(request, 'index.html', data)


def product_details(request, product_id):
    data = {
        'title': 'Sabadiaz Jewelry - Product Details',
        'option': 'product'
    }
    return render(request, 'product_details.html', data)


def shop(request):
    data = {
        'title': 'Sabadiaz Jewelry - Shop',
        'option': 'shop'
    }
    return render(request, 'shop.html', data)


def about(request):
    data = {
        'title': 'Sabadiaz Jewelry - About Us',
        'option': 'about'
    }
    return render(request, 'about.html', data)


def contact(request):
    data = {
        'title': 'Sabadiaz Jewelry - Contact Us',
        'option': 'contact'
    }
    return render(request, 'contact.html', data)


def wishlist(request):
    data = {
        'title': 'Sabadiaz Jewelry - WishList',
        'option': 'wishlist'
    }
    return render(request, 'wishlist.html', data)