from django.urls import path
from .views import remove_cart_items, CartView

app_name = "cart"

urlpatterns = [
    path("", CartView.as_view(), name="cart"),
    path("delete", remove_cart_items, name="delete_item"),
]
