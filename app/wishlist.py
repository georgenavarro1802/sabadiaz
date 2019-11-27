import datetime

from django.db import transaction
from django.shortcuts import render

from app.helpers import ok_json, bad_json
from app.models import WishList
from app.views import addUserData


def view(request):
    data = {'title': 'Sabadiaz Jewelry - WishList'}
    addUserData(request, data)
    data['option'] = 'wishlist'
    data['current_page'] = 'Wishlist'
    data['my_wishlist'] = WishList.objects.filter(user=data['user'])
    return render(request, 'site/wishlist.html', data)


def add(request, product_id):
    data = {'title': 'Sabadiaz Jewelry - WishList - Add Item'}
    addUserData(request, data)

    try:
        with transaction.atomic():
            wishlist, _ = WishList.objects.get_or_create(user=data['user'], product_id=product_id)
            wishlist.created_at = datetime.datetime.now()
            wishlist.save()
            wishlist_items = WishList.objects.filter(user=data['user']).count()
            return ok_json(data={'message': 'Product added to your wishlist',
                                 'wishlist_items': wishlist_items})

    except Exception as ex:
        return bad_json(message=ex.__str__())


def delete(request, item_id):
    data = {'title': 'Sabadiaz Jewelry - WishList - Delete Item'}
    addUserData(request, data)

    try:
        with transaction.atomic():
            wishlist = WishList.objects.get(id=item_id)
            wishlist.delete()
            return ok_json(data={'message': 'Product removed from your wishlist'})

    except Exception as ex:
        return bad_json(message=ex.__str__())