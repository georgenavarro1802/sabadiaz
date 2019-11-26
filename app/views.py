from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from app.helpers import ok_json, bad_json
from app.models import Product, Slide, Category, Company, Testimonial, Material, Gender


def addUserData(request, data):
    data['user'] = request.user
    data['company'] = Company.objects.first()


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


def products(request):
    data = {'title': 'Sabadiaz Jewelry - Our Products'}
    addUserData(request, data)

    products = Product.objects.filter(stock__gt=0)

    category_ids = None
    if 'c' in request.GET and request.GET['c']:
        category_ids = [int(x) for x in request.GET['c'].split(',')]

    material_ids = None
    if 'm' in request.GET and request.GET['m']:
        material_ids = [int(x) for x in request.GET['m'].split(',')]

    gender_ids = None
    if 'g' in request.GET and request.GET['g']:
        gender_ids = [int(x) for x in request.GET['g'].split(',')]

    is_new = False
    if 'cn' in request.GET and request.GET['cn'] == 'true':
        is_new = True

    is_featured = False
    if 'cf' in request.GET and request.GET['cf'] == 'true':
        is_featured = True

    is_bestseller = False
    if 'cb' in request.GET and request.GET['cb'] == 'true':
        is_bestseller = True

    price_range = None
    if 'p' in request.GET and request.GET['p']:
        price_range = request.GET['p'].strip().replace('$', '').split(',')

    if category_ids:
        products = products.filter(category_id__in=category_ids)

    if material_ids:
        products = products.filter(material_id__in=material_ids)

    if gender_ids:
        products = products.filter(gender_id__in=gender_ids)

    if is_new:
        products = products.filter(is_new=True)

    if is_featured:
        products = products.filter(is_featured=True)

    if is_bestseller:
        products = products.filter(is_bestseller=True)

    if price_range:
        products = products.filter(price__gte=float(price_range[0]), price__lte=float(price_range[1]))

    page = request.GET.get('page', 1)

    paginator = Paginator(products, 12)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    data['products'] = products

    data['option'] = 'products'
    data['current_page'] = 'Our Products'
    data['categories'] = Category.objects.filter(product__stock__gt=0).distinct().order_by('id')
    data['materials'] = Material.objects.filter(product__stock__gt=0).distinct().order_by('id')
    data['genders'] = Gender.objects.filter(product__stock__gt=0).distinct().order_by('id')
    data['category_ids'] = category_ids
    data['gender_ids'] = gender_ids
    data['material_ids'] = material_ids
    data['is_new'] = is_new
    data['is_featured'] = is_featured
    data['is_bestseller'] = is_bestseller
    data['products'] = products
    return render(request, 'site/products.html', data)


def contact(request):
    data = {'title': 'Sabadiaz Jewelry - Contact Us'}
    addUserData(request, data)
    data['option'] = 'contact'
    data['current_page'] = 'Contact'
    return render(request, 'site/contact.html', data)


def wishlist(request):
    data = {'title': 'Sabadiaz Jewelry - WishList'}
    addUserData(request, data)
    data['option'] = 'wishlist'
    data['current_page'] = 'Wishlist'
    return render(request, 'site/wishlist.html', data)


def product_details(request, product_id):
    data = {'title': 'Sabadiaz Jewelry - Product Details'}
    addUserData(request, data)
    data['option'] = 'product'
    data['current_page'] = 'Product Details'
    data['product'] = Product.objects.get(id=product_id)
    return render(request, 'site/product_details.html', data)


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


def account(request):
    data = {'title': 'Sabadiaz Jewelry - My Account'}
    addUserData(request, data)
    data['option'] = 'My Account'
    data['current_page'] = 'My Account'
    return render(request, 'account.html', data)


def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/")
