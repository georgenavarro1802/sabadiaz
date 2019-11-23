import time

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db import transaction
from django.shortcuts import render
from django.urls import reverse

from app.helpers import GENDERS, ok_json, bad_json, MATERIALS
from app.models import Product, Category


def view(request):
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
                  'administration/products/view.html',
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
        'materials': MATERIALS,
        'genders': GENDERS,
        'categories': Category.objects.all(),
        'product': None
    }

    if request.method == 'POST':
        try:
            with transaction.atomic():
                title = request.POST['title']
                description = request.POST['description']
                category_id = int(request.POST['category_id'])
                gender = int(request.POST['gender'])
                material = int(request.POST['material'])
                price = float(request.POST['price'])
                stock = int(request.POST['stock'])
                discount = float(request.POST['discount'])
                vprice = float(request.POST['vprice'])
                information = request.POST['information']
                is_new = True if request.POST['is_new'] == 'on' else False
                is_featured = True if request.POST['is_featured'] == 'on' else False
                is_bestseller = True if request.POST['is_bestseller'] == 'on' else False
                is_onsale = True if request.POST['is_onsale'] == 'on' else False

                product = Product(category_id=category_id,
                                  gender=gender,
                                  material=material,
                                  title=title,
                                  description=description,
                                  information=information,
                                  price=price,
                                  v_price=vprice,
                                  p_discount=discount,
                                  stock=stock,
                                  is_new=is_new,
                                  is_featured=is_featured,
                                  is_bestseller=is_bestseller,
                                  is_onsale=is_onsale)
                product.save()

                for index, key in enumerate(request.FILES):
                    setattr(product, f'image{index+1}', request.FILES[key])
                    product.save()

                time.sleep(1)
                return ok_json(data={'message': 'Product has been succesfully created!',
                                     'redirect_url': reverse('admin_products')})

        except Exception as ex:
            return bad_json(message=ex.__str__())

    return render(request, 'administration/products/product.html', data)


def edit_product(request, product_id):
    product = Product.objects.get(id=product_id)

    data = {
        'title': 'Sabadiaz Jewelry Admin - Edit Product',
        'option': 'admin_edit_product',
        'user': request.user,
        'materials': MATERIALS,
        'genders': GENDERS,
        'categories': Category.objects.all(),
        'product': product
    }

    if request.method == 'POST':
        try:
            with transaction.atomic():
                product.title = request.POST['title']
                product.description = request.POST['description']
                product.category_id = int(request.POST['category_id'])
                product.gender = int(request.POST['gender'])
                product.material = int(request.POST['material'])
                product.price = float(request.POST['price'])
                product.stock = int(request.POST['stock'])
                product.discount = float(request.POST['discount'])
                product.vprice = float(request.POST['vprice'])
                product.information = request.POST['information']
                product.is_new = True if request.POST['is_new'] == 'on' else False
                product.is_featured = True if request.POST['is_featured'] == 'on' else False
                product.is_bestseller = True if request.POST['is_bestseller'] == 'on' else False
                product.is_onsale = True if request.POST['is_onsale'] == 'on' else False
                product.save()

                time.sleep(1)
                return ok_json(data={'message': 'Product has been succesfully edited!',
                                     'redirect_url': reverse('admin_products')})

        except Exception as ex:
            return bad_json(message=ex.__str__())

    return render(request, 'administration/products/product.html', data)


def delete_product(request, product_id):
    data = {
        'title': 'Sabadiaz Jewelry Admin - Delete Product',
        'option': 'admin_delete_product',
        'user': request.user,
    }
    if request.method == 'POST':
        try:
            with transaction.atomic():
                product = Product.objects.get(id=product_id)
                product.delete()
                return ok_json(data={'message': 'Product has been succesfully deleted!',
                                     'redirect_url': reverse('admin_products')})

        except Exception as ex:
            return bad_json(message=ex.__str__())

    return render(request, 'administration/products/product.html', data)


def delete_product_image(request, product_id, image_id):
    data = {
        'title': 'Sabadiaz Jewelry Admin - Delete Product Image',
        'option': 'admin_delete_product_image',
        'user': request.user,
    }

    if request.method == 'POST':
        try:
            with transaction.atomic():
                product = Product.objects.get(id=product_id)
                setattr(product, f'image{image_id}', None)
                product.save()
                return ok_json(data={'message': 'Image succesfully deleted!'})

        except Exception as ex:
            return bad_json(message=ex.__str__())

    return render(request, 'administration/products/product.html', data)


def edit_product_image(request, product_id, image_id):
    data = {
        'title': 'Sabadiaz Jewelry Admin - Edit Product Image',
        'option': 'admin_delete_product_image',
        'user': request.user,
    }

    if request.method == 'POST':
        try:
            with transaction.atomic():
                product = Product.objects.get(id=product_id)
                setattr(product, f'image{image_id}', request.FILES['file'])
                product.save()
                return ok_json(data={'message': f'Image {image_id} succesfully edited!'})

        except Exception as ex:
            return bad_json(message=ex.__str__())

    return render(request, 'administration/products/product.html', data)
