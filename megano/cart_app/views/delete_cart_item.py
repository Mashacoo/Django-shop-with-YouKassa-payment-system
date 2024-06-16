import inject
from django.shortcuts import redirect
from cart_app.interfaces.cart_item_interface import ICartItem
from cart_app.models import CartItem
_cart_item: ICartItem = inject.attr(ICartItem)


def remove_cart_items(request):
    """
    Функция удаления продукта из корзины
    """
    data = request.GET
    if request.user.is_authenticated:
        CartItem.objects.get(product__id=data['product_id'], seller__id=data['seller_id']).delete()
    else:
        cart = request.session['cart']
        for item in cart:
            if item['product_id'] == int(data['product_id']) and item['seller_id'] == int(data['seller_id']):
                cart.remove(item)
                break
        request.session['cart'] = cart
    return redirect('cart:cart')
