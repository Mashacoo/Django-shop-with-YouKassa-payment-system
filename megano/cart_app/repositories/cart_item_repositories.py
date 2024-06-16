from beartype import beartype
from django.core.exceptions import ObjectDoesNotExist
from cart_app.interfaces.cart_item_interface import ICartItem
from cart_app.models import CartItem, Cart
from django.db.models import QuerySet
from typing import Optional


class CartItemRepository(ICartItem):
    """Для реализации методов взаимодействия с данными
    модели CartItem на основании интерфейса ICartItem"""

    @beartype
    def save(self, model: CartItem) -> None:
        """Сохранить экземпляр модели CartItem"""
        model.save()

    @beartype
    def delete(self, product_id: int, seller_id: int) -> None:
        """
        Удалить экземпляр модели CartItem
        """
        CartItem.objects.get(product__id=product_id, seller__id=seller_id).delete()

    @beartype
    def get_cart_item_by_product_and_seller(self, product_id: int, seller_id: int) -> Optional[CartItem]:
        """
        Получить экземпляры модели CartItem по id продукта и продавца
        """
        try:
            return CartItem.objects.get(product__id=product_id, seller__id=seller_id)
        except ObjectDoesNotExist:
            return None

    @beartype
    def get_items_for_calc_total_amount_cart(self, cart: Cart) -> QuerySet[CartItem]:
        """Получить экземпляры модели CartItem связанные с корзиной cart,
        для расчёта общей стоимости корзины"""
        return CartItem.objects.filter(cart=cart).all().select_related('product', 'seller')

    @beartype
    def get_cart_items(self, user_pk):
        return CartItem.objects.filter(cart__user=user_pk)

    @beartype
    def delete_cart_item_from_cart(self, cart_item):
        cart_item.delete()


    @beartype
    def get_all_items_in_cart(self, cart: Cart) -> QuerySet[CartItem]:
        """
        Получить экземпляры модели CartItem связанные с корзиной cart
        """
        return CartItem.objects.filter(cart=cart)

    @beartype
    def sum_all_items_in_cart(self, cart: Cart) -> int:
        """Получить количество товаров в корзине
        """
        return sum([item.quantity for item in CartItem.objects.filter(cart=cart)])
