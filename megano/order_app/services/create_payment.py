"""
Сценарий проведения платежа
Пользователь переходит к оплате.
Вы отправляете ЮKassa запрос на создание платежа.
ЮKassa возвращает вам созданный объект платежа с токеном для инициализации виджета.
Вы инициализируете виджет и отображаете форму на странице оплаты или во всплывающем окне.
Пользователь выбирает способ оплаты, вводит данные.
При необходимости виджет перенаправляет пользователя на страницу подтверждения платежа или отображает всплывающее окно (например, для аутентификации по 3‑D Secure).
Пользователь подтверждает платеж.
Если по какой-то причине платеж не прошел (например, не хватило денег) и срок действия токена для инициализации виджета еще не истек, виджет отображает пользователю сообщение об ошибке и предлагает оплатить еще раз с возможностью повторно выбрать способ оплаты.
Если пользователь подтвердил платеж или если закончился срок действия токена для инициализации, виджет перенаправляет пользователя на страницу завершения оплаты на вашей стороне или выполняет действия, настроенные вами для события завершения оплаты.
Вы отображаете нужную информацию, в зависимости от статуса платежа.
Готово!

"""
import os

import var_dump as var_dump
from yookassa import Payment, Configuration
import inject
from order_app.interface.order_interface import IOrder
from megano.settings import URL_FOR_PAYMENT, PAYMENT_ACCOUNT_ID, PAYMENT_SECRET_KEY


Configuration.configure(PAYMENT_ACCOUNT_ID, PAYMENT_SECRET_KEY)
URL = URL_FOR_PAYMENT


class OrderPayment:

    _order: IOrder = inject.attr(IOrder)

    @classmethod
    def payment_create(cls,order_pk):

        order = cls._order.get_order_by_pk(order_pk)

        return_url = f'{URL}/order/{order.pk}/'

        res = Payment.create(
            {
                "amount": {
                    "value": order.total_amount,
                    "currency": "RUB"
                },
                "confirmation": {
                    "type": "redirect",
                    "return_url": return_url,
                },
                "capture": True,
                "description": f"Заказ №{order.pk}",
                "metadata": {
                    'orderNumber': order.pk,
                    'user_id': order.user.id,
                },
            })

        order.payment_id = res.id
        cls._order.save(order)
        var_dump.var_dump(res)

        return res

