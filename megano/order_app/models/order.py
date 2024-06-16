from django.db import models


from coreapp.models.basemodel import BaseModel
from auth_app.models.user import User
from coreapp.choices.delivery_choices import DELIVERY_CHOICES
from coreapp.choices.payment_type import PAYMENT_TYPE_CHOICES
from coreapp.choices.payment_status import PAYMENT_STATUS_CHOICES


class Order(BaseModel):

    """ Модель заказа """

    fio = models.CharField(max_length=50, verbose_name='fio')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders', verbose_name='order')
    delivery_type = models.CharField(max_length=20, choices=DELIVERY_CHOICES, default='ordinary', verbose_name="delivery_type")
    city = models.CharField(max_length=30, null=True, blank=True, verbose_name='city')
    address = models.TextField(max_length=100, null=True, blank=True, verbose_name='address')
    payment_type = models.CharField(max_length=20, choices=PAYMENT_TYPE_CHOICES,
                                    default='online', verbose_name="payment_type")
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES,
                                      default="unpaid", verbose_name="payment_status")
    total_amount = models.DecimalField(max_digits=20, blank=True, null=False, decimal_places=2,
                                       verbose_name='total_amount')
    payment_id = models.CharField(max_length=50, verbose_name='payment_id')


