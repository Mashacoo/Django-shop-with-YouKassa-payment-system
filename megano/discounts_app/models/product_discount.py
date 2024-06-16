from django.db import models
from discounts_app.models.base_discount import BaseDiscount
from catalog.models import Product
from profile_app.models.seller import Seller


class ProductDiscount(BaseDiscount):

    """Модель скидки на товар """

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_discounts')
    seller = models.ManyToManyField(Seller, related_name='product_discounts')

    class Meta:
        verbose_name = 'product discount'
        verbose_name_plural = 'product discounts'
