import datetime
import json

from django.http import HttpResponse


def bad_json(message=None):
    """
    Bad JSON response
    :param message:
    :return:
    """
    data = {
        'result': 'bad',
        'message': message
    }
    return HttpResponse(json.dumps(data), content_type="application/json")


def ok_json(data=None):
    """
    Success JSON response
    :param data:
    :return:
    """
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


