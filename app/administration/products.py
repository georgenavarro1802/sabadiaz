import time

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db import transaction
from django.shortcuts import render
from django.urls import reverse

from app.helpers import ok_json, bad_json
from app.models import Product, Category, Material, Gender
from app.views import addUserData


def view(request):
    data = {'title': 'Sabadiaz Jewelry Admin - All Products'}
    addUserData(request, data)

    products = Product.objects.order_by('-id')
    page = request.GET.get('page', 1)

    paginator = Paginator(products, 5)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    data['products'] = products
    data['option'] = 'admin_all_products'
    return render(request, 'administration/products/view.html', data)


def create_product(request):
    data = {'title': 'Sabadiaz Jewelry Admin - Create Product'}
    addUserData(request, data)

    if request.method == 'POST':
        try:
            with transaction.atomic():
                title = request.POST['title']
                description = request.POST['description']
                category_id = int(request.POST['category_id'])
                gender_id = int(request.POST['gender_id'])
                material_id = int(request.POST['material_id'])
                price = float(request.POST['price'])
                stock = int(request.POST['stock'])
                discount = float(request.POST['discount'])
                vprice = float(request.POST['vprice'])
                is_new = True if request.POST['is_new'] == 'true' else False
                is_featured = True if request.POST['is_featured'] == 'true' else False
                is_bestseller = True if request.POST['is_bestseller'] == 'true' else False

                product = Product(category_id=category_id,
                                  material_id=material_id,
                                  gender_id=gender_id,
                                  title=title,
                                  description=description,
                                  price=price,
                                  v_price=vprice,
                                  p_discount=discount,
                                  stock=stock,
                                  is_new=is_new,
                                  is_featured=is_featured,
                                  is_bestseller=is_bestseller)
                product.save()

                for index, key in enumerate(request.FILES):
                    setattr(product, f'image{index+1}', request.FILES[key])
                    setattr(product, f'image{index+1}_b', request.FILES[key])
                    product.save()

                time.sleep(1)
                return ok_json(data={'message': 'Product has been succesfully created!',
                                     'redirect_url': reverse('admin_products')})

        except Exception as ex:
            return bad_json(message=ex.__str__())

    data['option'] = 'admin_create_product'
    data['categories'] = Category.objects.all()
    data['materials'] = Material.objects.all()
    data['genders'] = Gender.objects.all()
    data['product'] = None
    return render(request, 'administration/products/product.html', data)


def edit_product(request, product_id):
    data = {'title': 'Sabadiaz Jewelry Admin - Edit Product'}
    addUserData(request, data)

    product = Product.objects.get(id=product_id)

    if request.method == 'POST':
        try:
            with transaction.atomic():
                product.category_id = int(request.POST['category_id'])
                product.material_id = int(request.POST['material_id'])
                product.gender_id = int(request.POST['gender_id'])
                product.title = request.POST['title']
                product.description = request.POST['description']
                product.stock = int(request.POST['stock'])
                product.price = float(request.POST['price'])
                product.vprice = float(request.POST['vprice'])
                product.discount = float(request.POST['discount'])
                product.is_new = True if request.POST['is_new'] == 'true' else False
                product.is_featured = True if request.POST['is_featured'] == 'true' else False
                product.is_bestseller = True if request.POST['is_bestseller'] == 'true' else False
                product.save()

                time.sleep(0.5)
                return ok_json(data={'message': 'Product has been succesfully edited!',
                                     'redirect_url': reverse('admin_products')})

        except Exception as ex:
            return bad_json(message=ex.__str__())

    data['option'] = 'admin_edit_product'
    data['categories'] = Category.objects.all()
    data['materials'] = Material.objects.all()
    data['genders'] = Gender.objects.all()
    data['product'] = product
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
                setattr(product, f'image{image_id}_b', request.FILES['file'])
                product.save()
                return ok_json(data={'message': f'Image {image_id} succesfully edited!'})

        except Exception as ex:
            return bad_json(message=ex.__str__())

    return render(request, 'administration/products/product.html', data)
