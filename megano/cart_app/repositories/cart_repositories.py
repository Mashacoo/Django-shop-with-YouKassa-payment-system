from typing import Optional
from beartype import beartype
from django.core.exceptions import ObjectDoesNotExist
from auth_app.models.user import User
from cart_app.interfaces.cart_interface import ICart
from cart_app.models import Cart


class CartRepository(ICart):
    """Для реализации методов взаимодействия с данными
    модели Cart на основании интерфейса ICart"""

    @beartype
    def get_cart_by_user(self, user: User) -> Optional[Cart]:
        """Получить экземпляр модели Cart"""
        try:
            cart = Cart.objects.get(user=user)
            return cart
        except ObjectDoesNotExist:
            return None

    @beartype
    def save(self, model: Cart) -> None:
        """Сохранить экземпляр модели Cart"""
        model.save()
