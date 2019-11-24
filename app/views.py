from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db import transaction
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from app.helpers import ok_json, bad_json
from app.models import Product, HomeSlider, Category


# Website Views
def index(request):
    data = {
        'title': 'Sabadiaz Jewelry - Welcome',
        'option': 'index',
        'user': request.user,
        'home_sliders': HomeSlider.objects.all(),
        'categories': Category.objects.filter(product__isnull=False)
    }
    return render(request, 'index.html', data)


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


def product_details(request, product_id):
    product = Product.objects.get(id=product_id)
    data = {
        'title': 'Sabadiaz Jewelry - Product Details',
        'option': 'product',
        'product': product
    }
    return render(request, 'product_details.html', data)


# Common Views
def login_user(request):
    data = {
        'title': 'Sabadiaz Jewelry - Log In',
        'option': 'Login',
        'user': request.user
    }
    if request.method == 'POST':
        try:
            user = authenticate(username=request.POST['email'].lower(), password=request.POST['password'])
            login(request, user)
            return ok_json(data={'message': f'Welcome {user.first_name}',
                                 'redirect_url': reverse('index'), })
        except Exception as ex:
            print(ex.__str__())
            return bad_json(message='Bad Credentials')

    return render(request, 'login.html', data)


def register(request):
    data = {
        'title': 'Sabadiaz Jewelry - Register',
        'option': 'Register'
    }
    if request.method == 'POST':
        try:
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            password1 = request.POST['password1']
            password2 = request.POST['password2']

            if first_name and last_name and email and password1 and password2:

                # Create User
                new_user, _ = User.objects.get_or_create(username=email, email=email)
                new_user.first_name = first_name
                new_user.last_name = last_name
                new_user.set_password(password1)
                new_user.save()

                # Login
                login(request, new_user)

                return ok_json(data={'message': f'Succesfull Registration. Welcome {new_user.first_name}',
                                     'redirect_url': reverse('index')})

            return bad_json(message='All fields are required')

        except Exception as ex:
            print(ex.__str__())
            return bad_json(message='Bad Credentials')

    return render(request, 'register.html', data)


def account(request):
    data = {
        'title': 'Sabadiaz Jewelry - My Account',
        'option': 'My Account',
        'user': request.user
    }
    return render(request, 'account.html', data)


def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/")
