from django.shortcuts import render
from order_app.interface.order_interface import IOrder
from django.http import HttpRequest, HttpResponse
import inject
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View


class HistoryOrdersView(View, LoginRequiredMixin):

    _order: IOrder = inject.attr(IOrder)

    def get(self, request: HttpRequest) -> HttpResponse:
        user = request.user
        orders = self._order.get_all_users_orders(user_pk=user.pk)
        return render(request,'order_app/historyorder.html', context={'orders': orders})
