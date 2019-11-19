from django.shortcuts import render


def view(request):
    data = {
        'title': 'Sabadiaz Jewelry - Administration Panel',
        'option': 'administration',
        'user': request.user
    }
    return render(request, 'administration/view.html', data)