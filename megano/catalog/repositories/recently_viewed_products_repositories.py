from typing import Optional
from beartype import beartype
from auth_app.models.user import User
from catalog.interfaces.recently_viewed_products_interface import IRecentlyViewedProducts
from catalog.models import Product
from catalog.models import RecentlyViewedProducts


class RecentlyViewedProductsRepository(IRecentlyViewedProducts):
    """Для реализации методов взаимодействия с данными
    модели RecentlyViewedProducts на основании интерфейса IRecentlyViewedProducts"""

    @beartype
    def get_recently_viewed_products_by_user_and_product(
            self, user: User, product: Product
    ) -> Optional[RecentlyViewedProducts]:
        """Получить экземпляр модели RecentlyViewedProducts
        с фильтрацией по полям user и product"""
        return RecentlyViewedProducts.objects.filter(user=user, product=product).first()

    @beartype
    def save(self, model: RecentlyViewedProducts) -> None:
        """Сохранить экземпляр модели RecentlyViewedProducts"""
        model.save()
