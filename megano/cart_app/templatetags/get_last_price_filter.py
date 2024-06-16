from django import template
from catalog.models import Price

register = template.Library()


@register.filter
def get_last_price(product_id, seller_id):
    """Выводит цену продукта"""
    price = Price.objects.filter(
        product_id=product_id,
        seller_id=seller_id
    ).last().price
    return price
