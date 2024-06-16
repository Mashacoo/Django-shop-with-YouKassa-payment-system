from decimal import Decimal, InvalidOperation
from django import template
from django.conf import settings

register = template.Library()


@register.filter
def first_image(product):
    return product.product_images.first()


@register.filter
def price_format(value):
    """Разделяет пробелами разряды цены, ограничивает двумя знаками
    после запятой и добавляет символ валюты"""
    try:
        decimal_value = Decimal(value)
        formatted_value = decimal_value.quantize(Decimal('.00'))
        return f'{formatted_value:,} {settings.CURRENCY_SYMBOL}'.replace(',', ' ')
    except (InvalidOperation, TypeError, ValueError):
        return f'0 {settings.CURRENCY_SYMBOL}'
