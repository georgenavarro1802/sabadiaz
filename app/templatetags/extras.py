# coding=utf-8
import random
from django import template
from django.forms import CheckboxInput


register = template.Library()


def grouped(l, n):
    # Yield successive n-sized chunks from l.
    for i in range(0, len(l), n):
        yield l[i:i+n]


def callmethod(obj, methodname):
    method = getattr(obj, methodname)
    if obj.__dict__.get("__callArg"):
        ret = method(*obj.__callArg)
        del obj.__callArg
        return ret
    return method()


def args(obj, arg):
    if not obj.__dict__.get("__callArg", ""):
        obj.__callArg = []
    obj.__callArg.append(arg)
    return obj


def suma(var, value=1):
    return var + value


def resta(var, value=1):
    return var - value


def divide(value, arg):
    return int(value) / int(arg) if arg else 0


def resto(value, arg):
    return int(value) % int(arg) if arg else 0


def porciento(value, arg):
    return round(value * 100 / float(arg), 2) if arg else 0


def calendarbox(var, dia):
    return var[dia]


def calendarboxdetails(var, dia):
    lista = var[dia]
    result = []
    for x in lista:
        b = [x.split(',')[0], x.split(',')[1]]
        result.append(b)
    return result


def calendarboxdetailsmostrar(var, dia):
    return var[dia]


def calendarboxdetails2(var, dia):
    lista = var[dia]
    result = []
    b = []
    for x in lista:
        b.append(x[0])
        b.append(x[1])
        result.append(b)
    return result


def calendarboxdetailssubir(var, dia):
    lista = var[dia]
    result = []
    b = []
    for x in lista:
        b.append(x[0])
        b.append(x[1])
        b.append(x[2])
        b.append(x[3])
        result.append(b)
    return result


def times(number):
    return range(number)


@register.filter(name='is_checkbox')
def is_checkbox(field):
    return field.field.widget.__class__.__name__ == CheckboxInput().__class__.__name__


@register.filter(name='times')
def times(number):
    return range(number)


@register.filter(name='extract')
def extract(dictionary, key):
    """
    Method used to extract values from dictionaries
    :param dictionary: Dictionary storing the information
    :param key: Key were the information is stored
    :return: The value stored in the key or None
    """
    return dictionary.get(key, None)


@register.filter(name='extract_from_object')
def extract_from_object(object, key):
    """
    Method used to extract field values from objects
    :param object: Object storing the information
    :param key: Key were the information is stored
    :return: The value stored in the key or None
    """
    return getattr(object, key, None)


@register.filter(name='replace')
def replace(value, args=","):
    try:
        old, new = args.split(',')
        return value.replace(old, new)
    except ValueError:
        return value


@register.filter(name="file_exists")
def file_exists(filename):
    from os import path
    return path.exists(filename)


@register.simple_tag
def generate_random_hex_code():
    return '#%02X%02X%02X' % (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


@register.filter
def cool_number(value, num_decimals=2):
    """
    Django template filter to convert regular numbers to a
    cool format (ie: 2K, 434.4K, 33M...)
    :param value: number
    :param num_decimals: Number of decimal digits
    """

    int_value = int(value)
    formatted_number = '{{:.{}f}}'.format(num_decimals)
    if int_value < 1000:
        return str(int_value)
    elif int_value < 1000000:
        return formatted_number.format(int_value/1000.0).rstrip('0.') + 'K'
    else:
        return formatted_number.format(int_value/1000000.0).rstrip('0.') + 'M'


@register.filter
def group_by(value, arg):
    return grouped(value, arg)


register.filter('times', times)
register.filter("call", callmethod)
register.filter("args", args)
register.filter("suma", suma)
register.filter("resta", resta)
register.filter("porciento", porciento)
register.filter("divide", divide)
register.filter("resto", resto)
register.filter("calendarbox", calendarbox)
register.filter("calendarboxdetails", calendarboxdetails)
register.filter("calendarboxdetails2", calendarboxdetails2)
register.filter("calendarboxdetailsmostrar", calendarboxdetailsmostrar)
register.filter("calendarboxdetailssubir", calendarboxdetailssubir)
register.filter("file_exists", file_exists)
