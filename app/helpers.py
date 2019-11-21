import datetime
import json

from django.http import HttpResponse


# CONSTANTS

GENDER_WOMEN = 1
GENDER_MEN = 2

GENDERS = (
    (GENDER_WOMEN, 'WOMEN'),
    (GENDER_MEN, 'MEN'),

)


# FUNCTIONS

def bad_json(message=None):
    data = {
        'result': 'bad',
        'message': message
    }
    return HttpResponse(json.dumps(data), content_type="application/json")


def ok_json(data=None):
    if data:
        if 'result' not in data.keys():
            data.update({"result": "ok"})
    else:
        data = {'result': 'ok'}
    return HttpResponse(json.dumps(data), content_type="application/json")


def generate_filename(prefix, original):
    """
    example: generate_filename("product_", nfile._name)
    :param prefix: str
    :param original: str
    :return:
    """
    return f"{prefix}_{datetime.datetime.today().strftime('%Y%m%d%f')}.{original.split('.')[-1]}"
