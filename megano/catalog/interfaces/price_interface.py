from abc import abstractmethod, ABC
from django.db.models import QuerySet
from catalog.models import Product, Price
from profile_app.models import Seller
from typing import List


class IPrice(ABC):
    """Интерфейс взаимодействия с данными модели Price"""

    @abstractmethod
    def get_prices_for_calc_total_amount_cart(
            self, products: list[Product], sellers: list[Seller]) -> QuerySet[Price]:
        """Получить экземпляры модели Price связанные с продуктами и продавцами из списков,
        для расчёта общей стоимости корзины"""
        pass

    @abstractmethod
    def get_prices_for_calc_total_amount_in_dto_cart(
            self, products: List[int], sellers: List[int]) -> QuerySet[Price]:
        """Получить экземпляры модели Price связанные с продуктами и продавцами из списков,
        для расчёта общей стоимости корзины для DTO"""
        pass

    @abstractmethod
    def get_price_for_product(self, product_id):
        """Получить цены на продукт"""
        pass