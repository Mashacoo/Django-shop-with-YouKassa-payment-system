from abc import abstractmethod
from order_app.models.order import Order
from cart_app.models import CartItem


class IOrderItem:

    @abstractmethod
    def get_order_items(self, order_pk):
        """Получить экземпляры модели OrderItems по конкретному заказу"""
        pass

    @abstractmethod
    def create_order_item(self, order, cart_item):
        """Cоздать экзeмпляр модели OrderItem"""
        pass
