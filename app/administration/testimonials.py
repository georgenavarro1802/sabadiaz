import time

from django.db import transaction
from django.shortcuts import render

from app.helpers import bad_json, ok_json
from app.models import Testimonial


def view(request):

    objects = Testimonial.objects.order_by('id')

    data = {
        'title': 'Sabadiaz Jewelry Admin - HomePage Testimonials',
        'option': 'admin_website_testimonials',
        'user': request.user,
        'testimonials': objects,
    }

    if request.method == 'POST':
        try:
            with transaction.atomic():
                # testimonial 1
                testimonial1 = objects[0]
                testimonial1.name = request.POST['testimonialname_1']
                testimonial1.testimonial_en = request.POST['testimonialtext_1_en']
                testimonial1.testimonial_es = request.POST['testimonialtext_1_es']
                testimonial1.save()

                # testimonial 2
                testimonial2 = objects[1]
                testimonial2.name = request.POST['testimonialname_2']
                testimonial2.testimonial_en = request.POST['testimonialtext_2_en']
                testimonial2.testimonial_es = request.POST['testimonialtext_2_es']
                testimonial2.save()

                # testimonial 3
                testimonial3 = objects[2]
                testimonial3.name = request.POST['testimonialname_3']
                testimonial3.testimonial_en = request.POST['testimonialtext_3_en']
                testimonial3.testimonial_es = request.POST['testimonialtext_3_es']
                testimonial3.save()

                # testimonial 4
                testimonial4 = objects[3]
                testimonial4.name = request.POST['testimonialname_4']
                testimonial4.testimonial_en = request.POST['testimonialtext_4_en']
                testimonial4.testimonial_es = request.POST['testimonialtext_4_es']
                testimonial4.save()

                time.sleep(1)
                return ok_json(data={'message': 'Testimonials updated!'})

        except Exception as ex:
            return bad_json(message=ex.__str__())

    return render(request, 'administration/testimonials/view.html', data)


def update_avatar(request, testimonial_id):

    try:
        with transaction.atomic():
            testimonial = Testimonial.objects.get(id=testimonial_id)
            testimonial.avatar = request.FILES['file']
            testimonial.save()
            return ok_json(data={'message': 'Avatar succesfully updated!'})

    except Exception as ex:
        return bad_json(message=ex.__str__())

