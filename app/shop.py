from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.shortcuts import render

from app.models import Product, Category, Material, Gender
from app.views import addUserData


def view(request):
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


def details(request, product_id):
    data = {'title': 'Sabadiaz Jewelry - Product Details'}
    addUserData(request, data)

    data['option'] = 'product_details'
    data['current_page'] = 'Product Details'
    data['product'] = product = Product.objects.get(id=product_id)

    data['related_products'] = Product.objects.filter(Q(category=product.category) |
                                                      Q(material=product.material) |
                                                      Q(gender=product.gender)).exclude(id=product_id)[:6]
    return render(request, 'site/product_details.html', data)
