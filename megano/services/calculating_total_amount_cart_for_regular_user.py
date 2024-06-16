from decimal import Decimal
import inject
from typing import List
from cart_app.utils import CartItemDTO
from catalog.interfaces.price_interface import IPrice


class CalculatingTotalAmountCart:
    """Класс для реализации методов расчёта общей стоимости корзины"""

    __price: IPrice = inject.attr(IPrice)

    def __init__(self, cart_items: List[CartItemDTO]) -> None:
        self.cart_items = cart_items

    def __call__(self) -> Decimal:
        """Метод расчёта общей стоимости корзины"""
        total_amount = Decimal("0.00")
        products = []
        sellers = []

        [(products.append(item.product.pk), sellers.append(item.seller.pk)) for item in self.cart_items]

        prices = self.__price.get_prices_for_calc_total_amount_in_dto_cart(
            products=products, sellers=sellers)
        prices_dict = {(price.product.pk, price.seller.pk): price for price in prices}

        for item in self.cart_items:
            price = prices_dict.get((item.product.pk, item.seller.pk))
            total_amount += item.quantity * price.price if price else 0
        return total_amount
