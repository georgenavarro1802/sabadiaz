import time

from django.db import transaction
from django.shortcuts import render

from app.helpers import bad_json, ok_json
from app.models import Slide


def view(request):

    objects = Slide.objects.order_by('id')

    data = {
        'title': 'Sabadiaz Jewelry Admin - HomePage Slides',
        'option': 'admin_website_slides',
        'user': request.user,
        'slides': objects,
    }

    if request.method == 'POST':
        try:
            with transaction.atomic():

                # slide 1
                slide1 = objects[0]
                slide1.text1_en = request.POST['text1_1_en']
                slide1.text2_en = request.POST['text2_1_en']
                slide1.description_en = request.POST['desc_1_en']
                slide1.text1_es = request.POST['text1_1_es']
                slide1.text2_es = request.POST['text2_1_es']
                slide1.description_es = request.POST['desc_1_es']
                slide1.save()

                # slide 2
                slide2 = objects[1]
                slide2.text1_en = request.POST['text1_2_en']
                slide2.text2_en = request.POST['text2_2_en']
                slide2.description_en = request.POST['desc_2_en']
                slide2.text1_es = request.POST['text1_2_es']
                slide2.text2_es = request.POST['text2_2_es']
                slide2.description_es = request.POST['desc_2_es']
                slide2.save()

                # slide 3
                slide3 = objects[2]
                slide3.text1_en = request.POST['text1_3_en']
                slide3.text2_en = request.POST['text2_3_en']
                slide3.description_en = request.POST['desc_3_en']
                slide3.text1_es = request.POST['text1_3_es']
                slide3.text2_es = request.POST['text2_3_es']
                slide3.description_es = request.POST['desc_3_es']
                slide3.save()

                time.sleep(1)
                return ok_json(data={'message': 'Homepage Slides updated!'})

        except Exception as ex:
            return bad_json(message=ex.__str__())

    return render(request, 'administration/slides/view.html', data)


def update_image(request, slide_id):

    try:
        with transaction.atomic():
            slide = Slide.objects.get(id=slide_id)
            slide.image = request.FILES['file']
            slide.save()
            return ok_json(data={'message': 'Image succesfully updated!'})

    except Exception as ex:
        return bad_json(message=ex.__str__())
