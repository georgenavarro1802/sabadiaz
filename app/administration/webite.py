from django.shortcuts import render

from app.models import HomeSlider


def home_sliders(request):

    return render(request, 'administration/website/home_sliders.html', {
        'title': 'Sabadiaz Jewelry Admin - HomePage Sliders',
        'option': 'admin_website_home_sliders',
        'user': request.user,
        'home_sliders': HomeSlider.objects.order_by('id'),
    })
