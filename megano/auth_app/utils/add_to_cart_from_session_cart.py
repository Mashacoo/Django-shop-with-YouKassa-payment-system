from services.add_products_to_cart import AddProductsToCart


def add_to_cart_from_session_cart(request):
    """
    Функция добавления списка товаров из сессий в корзину
    """
    for item in request.session['cart']:
        AddProductsToCart(user=request.user)(
            quantity=item['num_products'],
            product_id=item['product_id'],
            seller_id=item['seller_id']
        )
    request.session['cart'] = []
