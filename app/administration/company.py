from django.db import transaction
from django.shortcuts import render

from app.helpers import ok_json, bad_json
from app.models import Company


def company_data(request):

    company = Company.objects.all()[0]

    if request.method == 'POST':
        try:
            with transaction.atomic():
                company.name = request.POST['c_name']
                company.description_en = request.POST['c_description_en']
                company.description_es = request.POST['c_description_es']
                company.address = request.POST['c_address']
                company.email = request.POST['c_email']
                company.phone = request.POST['c_phone']
                company.facebook = request.POST['c_facebook']
                company.twitter = request.POST['c_twitter']
                company.instagram = request.POST['c_instagram']
                company.youtube = request.POST['c_youtube']
                company.save()
                return ok_json(data={'message': 'Company data updated!'})

        except Exception as ex:
            return bad_json(message=ex.__str__())

    return render(request,
                  'administration/company/view.html',
                  {
                      'title': 'Sabadiaz Jewelry Admin - HomePage Sliders',
                      'option': 'admin_website_company_data',
                      'user': request.user,
                      'company': company,
                  })


def company_logo(request):
    company = Company.objects.first()

    try:
        with transaction.atomic():
            company.logo = request.FILES['file']
            company.save()
            return ok_json(data={'message': 'Logo updated!'})

    except Exception as ex:
        return bad_json(message=ex.__str__())