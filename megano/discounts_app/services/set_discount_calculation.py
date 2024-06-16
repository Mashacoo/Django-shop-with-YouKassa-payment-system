from discounts_app.services.cart_discount_calculations import CartDiscountCalculations
import inject
from discounts_app.interfaces.discounts_interface import IDiscounts


class SetDiscountsCalculations:
    _discount: IDiscounts = inject.attr(IDiscounts)

    @classmethod
    def check_discount_implementation(cls, cart: list):

        """
        Проверяет соблюдение условий применения скидки на наборы
        discounts_to_apply = список из вложенных словарей [QuerySet: SetDiscount: [id_1, id_2]] ,
         где id_1, id_2 id продуктов в группе 1 и 2 соответственно
        """

        discount_details = cls._discount.get_all_active_set_discounts()
        discounts_to_apply = []
        if discount_details:
            for discount in discount_details:
                item_list = []

                for item in cart:

                    if discount.product_set.group_1.all().filter(id=item['product_id']):
                        item_list.append(item['product_id'])

                    elif discount.product_set.group_2.all().filter(id=item['product_id']):
                        item_list.append(item['product_id'])

                if len(item_list) >= 2:
                    discounts_to_apply.append({discount: item_list})

            if len(discounts_to_apply) > 0:
                return discounts_to_apply

            else:
                return False
        else:
            return None

    @classmethod
    def apply_set_discount(cls, cart: list):
        """
        Функция производит расчет минимальной стоимости корзины с учетом максимально возможной скидки на наборы
        """

        set_disc = cls.check_discount_implementation(cart)
        if set_disc is not None and set_disc is not False:
            total_sum_of_cart = []

            if set_disc is not None:
                for discount in set_disc:
                    prices_for_disc = 0
                    for key, values in discount.items():
                        for id_product in values:
                            for item in cart:
                                if item['product_id'] == id_product:
                                    prices_for_disc += item['price']
                                    cart.remove(item)
                        result = (CartDiscountCalculations.calculate_cart_sum(cart) + CartDiscountCalculations.
                                  apply_discount(key, prices_for_disc))
                        total_sum_of_cart.append(result)
                        print(total_sum_of_cart)
                return min(total_sum_of_cart)

            else:
                return None
        else:
            return None
