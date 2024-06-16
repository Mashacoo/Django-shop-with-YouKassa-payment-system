from typing import Optional
from beartype import beartype
from django.core.exceptions import ObjectDoesNotExist
from auth_app.models import User
from profile_app.interfaces.seller_interface import ISeller
from profile_app.models.seller import Seller


class SellerRepository(ISeller):
    """Для реализации методов взаимодействия с данными
    модели Seller на основании интерфейса ISeller"""

    @beartype
    def get_seller(self, pk: int) -> Optional[Seller]:
        """Получить экземпляр модели Product"""
        try:
            return Seller.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return None

    @beartype
    def get_seller_by_user(self, user: User) -> Optional[Seller]:
        """Получить экземпляр модели Seller связанный с экземпляром модели User"""
        try:
            return Seller.objects.get(user=user)
        except ObjectDoesNotExist:
            return None
