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
        'product': None
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
        'product': Product.objects.get(id=product_id)
    }
    return render(request, 'administration/product.html', data)


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

    return render(request, 'administration/product.html', data)


def delete_product_image(request, product_id, image_id):
    data = {
        'title': 'Sabadiaz Jewelry Admin - Delete Product',
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

    return render(request, 'administration/product.html', data)


def images(request, product_id):
    product = Product.objects.get(id=product_id)
    return ok_json(data={'images': product.get_images_list(), 'username': request.user.username})

# if (jQuery.isEmptyObject(data.results)){
#                                 inputPurchaserNameAddLine.val('');
#                                 inputPurchaserAddress1AddLine.val('');
#                                 inputPurchaserAddress2AddLine.val('');
#                                 inputPurchaserCityAddLine.val('');
#                                 inputPurchaserStateAddLine.val('');
#                                 inputPurchaserZipAddLine.val('');
#                                 return ''
#                             }else{
#                                 result($.map(data, function (item) {
#                                     # inputPurchaserNameAddLine.val(item.company_name);
# # inputPurchaserAddress1AddLine.val(item.address1);
# # inputPurchaserAddress2AddLine.val(item.address2);
# # inputPurchaserCityAddLine.val(item.city);
# # inputPurchaserStateAddLine.val(item.state);
# # inputPurchaserZipAddLine.val(item.zip_code);
#                                 }));
#                             }

