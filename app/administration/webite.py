import time

from django.db import transaction
from django.shortcuts import render

from app.helpers import bad_json, ok_json
from app.models import HomeSlider


def home_sliders(request):

    objects = HomeSlider.objects.order_by('id')

    data = {
        'title': 'Sabadiaz Jewelry Admin - HomePage Sliders',
        'option': 'admin_website_home_sliders',
        'user': request.user,
        'home_sliders': objects,
    }

    if request.method == 'POST':
        try:
            with transaction.atomic():
                # slide 1
                slide1 = objects[0]
                slide1.text1 = request.POST['text1_1']
                slide1.text2 = request.POST['text2_1']
                slide1.description = request.POST['desc_1']
                slide1.save()
                # TODO: add image

                # slide 2
                slide2 = objects[1]
                slide2.text1 = request.POST['text1_2']
                slide2.text2 = request.POST['text2_2']
                slide2.description = request.POST['desc_2']
                slide2.save()

                # slide 3
                slide3 = objects[2]
                slide3.text1 = request.POST['text1_3']
                slide3.text2 = request.POST['text2_3']
                slide3.description = request.POST['desc_3']
                slide3.save()

                time.sleep(1)
                return ok_json(data={'message': 'Homepage slides updated!'})

        except Exception as ex:
            return bad_json(message=ex.__str__())

    return render(request, 'administration/website/home_sliders.html', data)


def home_sliders_update_image(request, hs_id):
    data = {
        'title': 'Sabadiaz Jewelry Admin - Update Home Slide Image',
        'option': 'admin_website_home_sliders_update_image',
        'user': request.user,
    }

    if request.method == 'POST':
        try:
            with transaction.atomic():
                hs = HomeSlider.objects.get(id=hs_id)
                hs.image = request.FILES['file']
                hs.save()
                return ok_json(data={'message': 'Image succesfully updated!'})

        except Exception as ex:
            return bad_json(message=ex.__str__())

    return render(request, 'administration/products/product.html', data)
