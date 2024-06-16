from typing import List
from dataclasses import dataclass
from decimal import Decimal


@dataclass
class Seller(object):
    """
    модель DTO для модели Seller
    """
    pk: int = 0
    name: str = ''


@dataclass
class Product(object):
    """
    модель DTO для модели Product
    """
    pk: int = 0
    title: str = ''
    description: str = ''
    image: str = ''
    product_discounts: int = 0


@dataclass
class CartItemDTO:
    """
    модель DTO для модели CartItem
    """
    seller: Seller
    product: Product
    quantity: int


@dataclass
class CartDTO:
    """
    модель DTO для модели Cart
    """
    cart_items: List[CartItemDTO]
    total_amount: Decimal
