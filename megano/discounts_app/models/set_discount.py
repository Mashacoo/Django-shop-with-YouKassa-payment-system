from django.db import models
from discounts_app.models.base_discount import BaseDiscount
from .product_set import ProductSet


class SetDiscount(BaseDiscount):

    """Модель скидки на набор """

    product_set = models.ForeignKey(ProductSet, on_delete=models.CASCADE, related_name='set_discounts')

    class Meta:
        verbose_name = 'set discount'
        verbose_name_plural = 'set discounts'
