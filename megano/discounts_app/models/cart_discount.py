from django.db import models
from discounts_app.models.base_discount import BaseDiscount


class CartDiscount(BaseDiscount):

    """Модель скидки на набор"""

    final_sum_min = models.PositiveIntegerField(null=True, blank=False, verbose_name='final_sum_min')
    final_sum_max = models.PositiveIntegerField(blank=True, verbose_name='final_sum_max', default=1000000)
    products_quantity = models.PositiveIntegerField(null=True, blank=True, verbose_name='product_quantity', default=0)

    class Meta:
        verbose_name = 'cart discount'
        verbose_name_plural = 'cart discounts'
