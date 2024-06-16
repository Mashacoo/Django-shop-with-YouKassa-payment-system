from catalog.models import Price
from services.add_products_to_cart import AddProductsToCart
from catalog.utils import add_product_to_session_cart


def add_product_from_catalog(request, price, product_id):
    """
    Функция добавления одного товара из каталога товаров в корзину
    """
    price = Price.objects.get(price=price, product_id=product_id)
    if request.user.is_authenticated:
        AddProductsToCart(user=request.user)(
            quantity=1,
            product_id=product_id,
            seller_id=price.seller.id
        )
    else:
        cart = request.session.get('cart', [])
        request.session['cart'] = add_product_to_session_cart(
            cart=cart,
            seller_id=price.seller.id,
            product_id=product_id,
            num_products=1
        )
