from abc import abstractmethod, ABC

from django.db.models import QuerySet

from cart_app.models import CartItem, Cart
from typing import Optional


class ICartItem(ABC):
    """Интерфейс взаимодействия с данными модели CartItem"""

    @abstractmethod
    def save(self, model: CartItem) -> None:
        """Сохранить экземпляр модели CartItem"""
        pass

    @abstractmethod
    def delete(self, product_id: int, seller_id: int) -> None:
        """
        Удалить экземпляр модели CartItem
        """
        pass

    @abstractmethod
    def get_cart_item_by_product_and_seller(self, product_id: int, seller_id: int) -> Optional[CartItem]:
        """
        Получить экземпляр модели CartItem по id продукта и продавца
        """
        pass

    @abstractmethod
    def get_items_for_calc_total_amount_cart(self, cart: Cart) -> QuerySet[CartItem]:
        """Получить экземпляры модели CartItem связанные с корзиной cart,
        для расчёта общей стоимости корзины"""
        pass

    @abstractmethod
    def get_all_items_in_cart(self, cart: Cart) -> QuerySet[CartItem]:
        """Получить экземпляры модели CartItem связанные с корзиной cart
        """
        pass

    @abstractmethod
    def sum_all_items_in_cart(self, cart: Cart) -> int:
        """Получить количество товаров в корзине
        """
        pass

    @abstractmethod
    def get_cart_items(self, user_pk):
        """Получить все экземпляры CartItem из корзины пользователя"""
        pass

    @abstractmethod
    def delete_cart_item_from_cart(self, model: CartItem):
        """Удаление элемента CartItem из корзины"""
        pass
