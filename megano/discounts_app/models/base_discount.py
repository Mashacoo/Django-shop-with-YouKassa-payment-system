from django.db import models
from coreapp.models.basemodel import BaseModel


class BaseDiscount(BaseModel):

    """Базовая модель скидки """

    CHOICES_TYPE = [
        ('per', 'Per cent'),
        ('fa', 'Fixed amount'),
        ('fp', 'Fixed price'),]

    name = models.CharField(max_length=30, null=True, blank=True, verbose_name='name')
    description = models.TextField(max_length=200, null=True, blank=True, verbose_name='description')
    type_of_discount = models.CharField(max_length=3, choices=CHOICES_TYPE, default='per', verbose_name='type')
    amount = models.DecimalField(decimal_places=2, max_digits=20, verbose_name="amount", default=0)

    class Meta:
        abstract = True
