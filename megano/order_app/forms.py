from django.forms import ModelForm
from order_app.models.order import Order

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['user', 'fio', 'delivery_type', 'city', 'address', 'payment_type', 'total_amount']

