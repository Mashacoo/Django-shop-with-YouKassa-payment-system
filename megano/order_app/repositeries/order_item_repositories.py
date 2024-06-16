from beartype import beartype
from order_app.models.order_item import OrderItem
from order_app.interface.order_item_interface import IOrderItem


class OrderItemRepository(IOrderItem):

    @beartype
    def get_order_items(self, order_pk):
        return OrderItem.objects.filter(order_id=order_pk)

    @beartype
    def create_order_item(self, order,cart_item):
        OrderItem.objects.create(
            order=order,
            product=cart_item.product,
            quantity=cart_item.quantity,
            seller=cart_item.seller)
