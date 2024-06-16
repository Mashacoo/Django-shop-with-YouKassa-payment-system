from decimal import Decimal

import inject

from cart_app.interfaces.cart_item_interface import ICartItem
from cart_app.models import Cart
from catalog.interfaces.price_interface import IPrice


class CalculatingTotalAmountCart:
    """Класс для реализации методов расчёта общей стоимости корзины"""

    __cart_item: ICartItem = inject.attr(ICartItem)
    __price: IPrice = inject.attr(IPrice)

    def __init__(self, cart: Cart) -> None:
        self.cart = cart

    def __call__(self) -> Decimal:
        """Метод расчёта общей стоимости корзины"""
        total_amount = Decimal("0.00")
        products = []
        sellers = []

        items = self.__cart_item.get_items_for_calc_total_amount_cart(cart=self.cart)
        [(products.append(item.product), sellers.append(item.seller)) for item in items]

        prices = self.__price.get_prices_for_calc_total_amount_cart(
            products=products, sellers=sellers)
        prices_dict = {(price.product, price.seller): price for price in prices}

        for item in items:
            price = prices_dict.get((item.product, item.seller))
            total_amount += item.quantity * price.price if price else 0
        return total_amount
