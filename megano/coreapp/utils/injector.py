import inject

from auth_app.interfaces.auth_interface import IAuth
from auth_app.repositories.auth_repositories import AuthRepository
from cart_app.interfaces.cart_interface import ICart
from cart_app.interfaces.cart_item_interface import ICartItem
from cart_app.repositories.cart_item_repositories import CartItemRepository
from cart_app.repositories.cart_repositories import CartRepository
from catalog.interfaces.catalog_interface import ICatalogRepository
from catalog.interfaces.comparison_list_interface import IComparisonList
from catalog.interfaces.price_interface import IPrice
from catalog.interfaces.product_interface import IProduct
from catalog.interfaces.recently_viewed_products_interface import IRecentlyViewedProducts
from catalog.interfaces.review_interface import IReview
from catalog.repositories.catalog_repositories import CatalogRepository
from catalog.repositories.comparison_list_repositories import ComparisonListRepository
from catalog.repositories.price_repositories import PriceRepository
from catalog.repositories.product_repositories import ProductRepository
from catalog.repositories.recently_viewed_products_repositories import \
    RecentlyViewedProductsRepository
from catalog.repositories.review_repositories import ReviewRepository
from coreapp.interfaces.core_interface import ICore
from coreapp.repositories.core_repositories import CoreRepository
from discounts_app.interfaces.discounts_interface import IDiscounts
from discounts_app.repositories.discounts_repositories import DiscountsRepository
from profile_app.interfaces import IProfile
from profile_app.interfaces.seller_interface import ISeller
from profile_app.repositories import ProfileRepository
from profile_app.repositories.seller_repositories import SellerRepository
from order_app.interface.order_interface import IOrder
from order_app.repositeries.order_repositories import OrderRepository
from order_app.interface.order_item_interface import IOrderItem
from order_app.repositeries.order_item_repositories import OrderItemRepository
from catalog.interfaces.category_interface import ICategory
from catalog.repositories.category_repositories import CategoryRepository

BINDS = (
    (IAuth, AuthRepository),
    (ICatalogRepository, CatalogRepository),
    (IProfile, ProfileRepository),
    (ICore, CoreRepository),
    (IDiscounts, DiscountsRepository),
    (IProduct, ProductRepository),
    (IPrice, PriceRepository),
    (IRecentlyViewedProducts, RecentlyViewedProductsRepository),
    (IReview, ReviewRepository),
    (ICart, CartRepository),
    (ICartItem, CartItemRepository),
    (ISeller, SellerRepository),
    (IComparisonList, ComparisonListRepository),
    (IOrder, OrderRepository),
    (IOrderItem, OrderItemRepository),
    (ICategory, CategoryRepository),

)


def config(binder):
    """Конфигуратор для inject."""
    for interface, implementation in BINDS:
        binder.bind(interface, implementation())


def configure_inject():
    """Конфигурирует зависимости для проекта."""
    inject.configure_once(config)
