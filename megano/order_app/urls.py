from django.urls import path
from .views.order_create_view import CreateOrderView
from .views.order_detail_view import OrderDetailView
from .views.webhooks_view import my_webhook_handler
from .views.history_order_view import HistoryOrdersView

urlpatterns = [
    path('', CreateOrderView.as_view(),name='order_create'),
    path('<int:pk>/', OrderDetailView.as_view(), name='order_details'),
    path('history/', HistoryOrdersView.as_view(), name='history'),
    path("payment-notification/", my_webhook_handler, name='webhook')
]
