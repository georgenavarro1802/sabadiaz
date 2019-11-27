from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from app.helpers import ok_json, bad_json
from app.models import Product, Slide, Category, Company, Testimonial, WishList


def addUserData(request, data):
    data['user'] = request.user
    data['is_visitor'] = '0' if request.user and request.user.is_anonymous else '1'
    data['company'] = Company.objects.first()
    data['wishlist_items'] = WishList.objects.filter(user=data['user']).count() if int(data['is_visitor']) else 0


# Website Views
def index(request):
    data = {'title': 'Sabadiaz Jewelry - Welcome'}
    addUserData(request, data)

    data['option'] = 'index'
    data['slides'] = Slide.objects.all()
    data['testimonials'] = Testimonial.objects.all()
    data['categories'] = Category.objects.filter(product__isnull=False).distinct()
    data['featured_products'] = Product.objects.filter(is_featured=True)[:10]
    data['bestseller_products'] = Product.objects.filter(is_bestseller=True)[:8]
    data['new_products'] = Product.objects.filter(is_new=True)[:8]
    return render(request, 'site/home.html', data)


def about(request):
    data = {'title': 'Sabadiaz Jewelry - About Us'}
    addUserData(request, data)
    data['option'] = 'about'
    data['current_page'] = 'About Us'
    data['testimonials'] = Testimonial.objects.all()
    return render(request, 'site/about.html', data)


def contact(request):
    data = {'title': 'Sabadiaz Jewelry - Contact Us'}
    addUserData(request, data)
    data['option'] = 'contact'
    data['current_page'] = 'Contact'
    return render(request, 'site/contact.html', data)


def account(request):
    data = {'title': 'Sabadiaz Jewelry - My Account'}
    addUserData(request, data)
    data['option'] = 'My Account'
    data['current_page'] = 'My Account'
    return render(request, 'account.html', data)


# Common Views
def login_user(request):
    data = {'title': 'Sabadiaz Jewelry - Log In'}
    addUserData(request, data)
    data['option'] = 'Login'

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
    data = {'title': 'Sabadiaz Jewelry - Register'}
    addUserData(request, data)
    data['option'] = 'Register'

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


def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/")
