from django.db import models
from coreapp.models.basemodel import BaseModel
from catalog.models import Product


class ProductSet(BaseModel):

    """Модель товарного набора"""

    group_1 = models.ManyToManyField(Product, related_name='group_1')
    group_2 = models.ManyToManyField(Product, related_name='group_2')

    class Meta:
        verbose_name = 'Set'
        verbose_name_plural = 'Sets'
