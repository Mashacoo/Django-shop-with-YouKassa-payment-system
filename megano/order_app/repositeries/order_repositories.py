from beartype import beartype
from order_app.interface.order_interface import IOrder
from order_app.models.order import Order


class OrderRepository(IOrder):

    @beartype
    def save(self, model):
        model.save()

    @beartype
    def get_order_by_pk(self, pk):
        return Order.objects.get(pk=pk)

    @beartype
    def get_all_users_orders(self, user_pk):
        return Order.objects.filter(user_id=user_pk)

    @beartype
    def get_all_orders(self):
        return Order.objects.all()

