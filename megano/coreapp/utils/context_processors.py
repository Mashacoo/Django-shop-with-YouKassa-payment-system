from services.calculating_total_amount_cart_for_regular_user import CalculatingTotalAmountCart
from cart_app.utils import CartDTO, CartItemDTO, FillingSeller, FillingProduct
from cart_app.models import CartItem


def quantity_products_and_total_amount_in_cart(request):
    """
    Функция получения информации об общей стоимости корзины, количестве товаров в ней и о самих товарах
    "amount_products_in_cart": Количество товаров в корзине,
    "total_amount_cart": Общая стоимость корзины,
    "cart": Экземпляр DTO модели 'Cart' которая содержит в себе все продукты
    """
    cart_items = list()
    amount_products_in_cart = 0

    if request.user.is_authenticated:
        """
        Получение продуктов из базы данных если пользователь авторизирован
        """
        for item in CartItem.objects.filter(cart=request.user.cart):
            product = FillingProduct().filling_from_db(item.product)
            seller = FillingSeller().filling_from_db(item.seller)
            amount_products_in_cart += item.quantity
            cart_items.append(CartItemDTO(seller=seller, product=product, quantity=item.quantity))
    else:
        """
            Получение продуктов из сессий если пользователь неавторизирован
        """
        if request.session.get('cart'):
            for item in request.session.get('cart'):
                amount_products_in_cart += item['num_products']
                product = FillingProduct().filling_from_session(item['product_id'])
                seller = FillingSeller().filling_from_session(item['seller_id'])
                cart_items.append(CartItemDTO(seller=seller, product=product, quantity=item['num_products']))
    cart = CartDTO(cart_items=cart_items, total_amount=CalculatingTotalAmountCart(cart_items)())

    if request.path == '/cart/':
        return {
            "amount_products_in_cart": amount_products_in_cart,
            "total_amount_cart": cart.total_amount,
            "cart": cart
        }
    else:
        return {
            "amount_products_in_cart": amount_products_in_cart,
            "total_amount_cart": cart.total_amount,
        }
