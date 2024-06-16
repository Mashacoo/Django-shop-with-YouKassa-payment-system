from beartype import beartype
from discounts_app.interfaces.discounts_interface import IDiscounts
from discounts_app.models.cart_discount import CartDiscount
from cart_app.models import CartItem
from catalog.models import Price
from discounts_app.models.product_discount import ProductDiscount
from discounts_app.models.set_discount import SetDiscount


class DiscountsRepository(IDiscounts):

    @beartype
    def get_all_active_cart_discounts(self):
        return CartDiscount.objects.filter(is_active=True).all()

    @beartype
    def get_cartitems_by_user_id(self, user_id):
        return CartItem.objects.values().filter(cart__user=user_id)

    @beartype
    def get_prices_by_group_of_products_ids(self, ids: list):
        return Price.objects.values().filter(product__id__in=ids)

    @beartype
    def get_all_active_product_discounts(self):
        return ProductDiscount.objects.all().filter(is_active=True)

    @beartype
    def get_all_active_set_discounts(self):
        return SetDiscount.objects.filter(is_active=True).all()
