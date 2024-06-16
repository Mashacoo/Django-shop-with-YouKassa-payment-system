from abc import abstractmethod, ABC
from typing import Optional
from auth_app.models.user import User
from catalog.models import Product
from catalog.models import RecentlyViewedProducts


class IRecentlyViewedProducts(ABC):
    """Интерфейс взаимодействия с данными модели RecentlyViewedProducts"""

    @abstractmethod
    def get_recently_viewed_products_by_user_and_product(
            self, user: User, product: Product
    ) -> Optional[RecentlyViewedProducts]:
        """Получить экземпляр модели RecentlyViewedProducts"""
        pass

    @abstractmethod
    def save(self, model: RecentlyViewedProducts) -> None:
        """Сохранить экземпляр модели RecentlyViewedProducts"""
        pass
