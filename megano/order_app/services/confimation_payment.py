from django.core.exceptions import ObjectDoesNotExist
import inject
from order_app.interface.order_interface import IOrder


class PaymentConfirmation:

    _order: IOrder = inject.attr(IOrder)

    @classmethod
    def confirm_payment(cls, payment_info):
        try:
            order_pk = int(payment_info.metadata['orderNumber'])
            order = cls._order.get_order_by_pk(pk=order_pk)

        except ObjectDoesNotExist:
            raise "Такого заказа нет"

        if payment_info.status == 'succeeded':
            order.payment_status = 'paid'
            cls._order.save(order)
            return True
        elif payment_info.status == 'canceled':
            order.payment_status = 'canceled'
            cls._order.save(order)
            return False

        else:
            raise Exception("Ошибка статуса платежа")

