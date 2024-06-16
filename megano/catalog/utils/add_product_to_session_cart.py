from typing import Dict, List


def add_product_to_session_cart(cart: List[Dict], product_id, seller_id, num_products):
    """
    Функция добавления товаров в сессионную корзину
    """
    for index in range(len(cart)):
        if cart[index]['product_id'] == product_id and cart[index]['seller_id'] != seller_id:
            cart[index]['num_products'] += num_products
            return cart

    cart.append({
        'product_id': product_id,
        'seller_id': seller_id,
        'num_products': num_products
    })
    return cart
