from django.db import models
from profile_app.models.seller import Seller
from catalog.models import Product
from django.utils.translation import gettext_lazy as _
from coreapp.models.basemodel import BaseModel
from .order import Order


class OrderItem(BaseModel):

    """Модель товара в Заказе пользователя"""
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="order_items",
        verbose_name="order_item"
    )
    seller = models.ForeignKey(
        Seller,
        on_delete=models.CASCADE,
        verbose_name=_("seller"),
        related_name="order_items",
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name=_("product"),
        related_name="order_items",
    )

    quantity = models.PositiveIntegerField(
        blank=True,
        null=False,
        default=1,
        verbose_name=_("quantity")
    )
