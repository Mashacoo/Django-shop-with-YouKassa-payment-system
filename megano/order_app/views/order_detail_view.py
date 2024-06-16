from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from order_app.interface.order_interface import IOrder
import inject
from order_app.services.create_payment import OrderPayment
from order_app.repositeries.order_item_repositories import IOrderItem


class OrderDetailView(TemplateView):

    _order: IOrder = inject.attr(IOrder)
    _order_item: IOrderItem = inject.attr(IOrderItem)

    template_name = "order_app/oneorder.html"
    context_object_name = "order"


    @method_decorator(csrf_exempt)
    def get_context_data(self, **kwargs):
        """Формирует контекст для шаблона"""
        order = self._order.get_order_by_pk(pk=self.kwargs['pk'])
        order_items = self._order_item.get_order_items(order_pk=order.pk)
        confirmation_url = ''
        if order.payment_status != "paid":
            payment = OrderPayment.payment_create(order_pk=order.pk)
            order.payment_id = payment.id
            self._order.save(order)
            confirmation_url = payment.confirmation.confirmation_url

        context = super().get_context_data(**kwargs)
        context['order'] = order
        context['order_items'] = order_items
        context['confirmation_url'] = confirmation_url
        return context
