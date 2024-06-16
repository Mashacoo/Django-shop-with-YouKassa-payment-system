import inject

from auth_app.models.user import User
from cart_app.interfaces.cart_interface import ICart
from cart_app.interfaces.cart_item_interface import ICartItem
from cart_app.models import CartItem
from catalog.interfaces.product_interface import IProduct
from profile_app.interfaces.seller_interface import ISeller


class AddProductsToCart:
    """Класс для реализации методов добавления товаров в корзину"""
    __product: IProduct = inject.attr(IProduct)
    __seller: ISeller = inject.attr(ISeller)
    __cart: ICart = inject.attr(ICart)
    __cart_item: ICartItem = inject.attr(ICartItem)

    def __init__(self, user: User) -> None:
        self.cart = self.__cart.get_cart_by_user(user=user)

    def __call__(self, quantity: int, product_id: int, seller_id: int) -> None:
        """Метод добавления товаров в корзину"""
        cart_item = self.__cart_item.get_cart_item_by_product_and_seller(product_id=product_id, seller_id=seller_id)
        if cart_item:
            cart_item.quantity += quantity
            self.__cart_item.save(cart_item)
        else:
            self.__cart_item.save(
                CartItem(
                    cart=self.cart,
                    product=self.__product.get_product(pk=product_id),
                    seller=self.__seller.get_seller(pk=seller_id),
                    quantity=quantity
                )
            )
