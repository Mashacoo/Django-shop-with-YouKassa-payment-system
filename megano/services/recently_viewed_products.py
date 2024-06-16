import inject

from auth_app.models.user import User
from catalog.interfaces.product_interface import IProduct
from catalog.interfaces.recently_viewed_products_interface import IRecentlyViewedProducts
from catalog.models import RecentlyViewedProducts


class RecentlyViewedProductsService:
    """Класс для реализации методов работы с недавно просмотренными товарами"""
    __product: IProduct = inject.attr(IProduct)
    __rec_view_products: IRecentlyViewedProducts = inject.attr(IRecentlyViewedProducts)

    def __init__(self, user: User) -> None:
        self.user = user

    def add(self, product_id: int) -> None:
        """Метод добавления продукта в список недавно просмотренных или обновления поля updated_at
        модели RecentlyViewedProducts если данный продукт ранее просматривался пользователем"""
        product = self.__product.get_product(pk=product_id)
        if view := self.__rec_view_products.get_recently_viewed_products_by_user_and_product(
                user=self.user,
                product=product
        ):
            self.__rec_view_products.save(model=view)
        else:
            self.__rec_view_products.save(
                model=RecentlyViewedProducts(
                    user=self.user, product=product
                )
            )
