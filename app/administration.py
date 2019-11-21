import time

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db import transaction
from django.shortcuts import render
from django.urls import reverse

from app.helpers import GENDERS, ok_json, bad_json
from app.models import Product, Category


def products(request):
    products = Product.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(products, 5)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return render(request,
                  'administration/products.html',
                  {
                      'title': 'Sabadiaz Jewelry Admin - All Products',
                      'option': 'admin_all_products',
                      'user': request.user,
                      'products': products,
                  })


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
        try:
            with transaction.atomic():
                title = request.POST['title']
                description = request.POST['description']
                category_id = int(request.POST['category_id'])
                gender = int(request.POST['gender'])
                price = float(request.POST['price'])
                stock = int(request.POST['stock'])
                discount = float(request.POST['discount'])
                vprice = float(request.POST['vprice'])
                information = request.POST['information']
                isnew = True if request.POST['isnew'] == 'on' else False

                product = Product(category_id=category_id,
                                  gender=gender,
                                  title=title,
                                  description=description,
                                  information=information,
                                  price=price,
                                  v_price=vprice,
                                  p_discount=discount,
                                  stock=stock,
                                  is_new=isnew)
                product.save()

                for index, key in enumerate(request.FILES):
                    setattr(product, f'image{index+1}', request.FILES[key])
                    product.save()

                time.sleep(1)
                return ok_json(data={'message': 'Product has been succesfully created!',
                                     'redirect_url': reverse('admin_products')})

        except Exception as ex:
            return bad_json(message=ex.__str__())

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
