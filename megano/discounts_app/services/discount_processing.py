# from megano.wsgi import *
from discounts_app.services.set_discount_calculation import SetDiscountsCalculations
from discounts_app.services.product_discount_calculation import ProductDiscountCalculations
from discounts_app.services.cart_discount_calculations import CartDiscountCalculations


"""Функция высчитывает скидки на товары

Одновременно может быть применена только одна скидка на корзину или на один набор в корзине.
Приоритет (вес) скидки указывается при редактировании скидки, применяется самая «тяжёлая» скидка.
Если к корзине не применена скидка ни на корзину, ни на набор,
то тогда на каждый товар по отдельности ищется скидка на товар,
при этом на каждый товар может быть применена только одна приоритетная скидка также по весу.

Скидки могут быть следующих видов:
Скидки на товар: скидки могут быть установлены на указанный список товаров и/или на указанные категории товаров.
 Например: Скидка 10% на все носки и шапку-ушанку.

Скидки на наборы: скидки могут быть установлены на группу товаров, если они вместе находятся в корзине.
 Указывается группа товаров 1 и группа товаров 2 (таким же образом, что и в скидке на товар,
 то есть раздел и/или конкретный товар). Если в корзине есть товар из первой и второй группы,
  то на эти два товара предоставляется скидка.
  Например: Купи чехол для паспорта и любую чугунную наковальню и получи скидку 1 000 рублей.

Скидки на корзину: скидки могут быть установлены на корзину,
например на количество товаров в корзине от-до и/или на общую стоимость товаров в корзине от-до.
Например: Собери 3-4 товара на сумму не менее 1 000 000 и купи это всё вместе за 37 рублей.
 Эта скидка применяется на итоговую стоимость товаров в корзине.


Механизм скидки может быть следующего вида:

Процент скидки ― в процентах от 1 до 99%.

Сумма скидки ― указывается фиксированный объём скидки, итоговая стоимость товара не может быть менее одного рубля.
 Если товар стоит 300 рублей, а скидка 400 рублей, то итоговая стоимость составляет один рубль, а не -100 рублей.

Фиксированная стоимость ― указывается итоговая стоимость от одного рубля, заменяет собой исходную цену.
"""


class DiscountProcessing:

    @classmethod
    def get_cart_sum_with_discounts(cls, user_id):
        """
        Функция рассчитывает итоговую стоимость корзины с применением скидок по условиям задания
        cart_sum_with_cart_discounts - применяются скидки типа CartDiscount
        cart_with_set_discounts - применяются скидки типа SetDiscount
        cart_with_products_discounts - применяются скидки типа ProductDiscount

        """
        final_sums = []
        cart_items = CartDiscountCalculations.get_items_with_prices(user_id=user_id)
        cart_without_discounts = CartDiscountCalculations.calculate_cart_sum(cart_items)

        cart_sum_with_cart_discounts = CartDiscountCalculations.apply_cart_discount(cart_items)
        if cart_sum_with_cart_discounts is not None and cart_sum_with_cart_discounts > 0:
            final_sums.append(cart_sum_with_cart_discounts)

        cart_with_set_discounts = SetDiscountsCalculations.apply_set_discount(cart_items)
        if cart_with_set_discounts is not None and cart_with_set_discounts > 0:
            final_sums.append(cart_with_set_discounts)

        if final_sums:
            return min(final_sums)

        else:
            cart_with_products_discounts = ProductDiscountCalculations.apply_product_discount(cart_items)
            if cart_with_products_discounts is not None and cart_with_products_discounts < cart_without_discounts:

                return cart_with_products_discounts
            else:

                return cart_without_discounts
