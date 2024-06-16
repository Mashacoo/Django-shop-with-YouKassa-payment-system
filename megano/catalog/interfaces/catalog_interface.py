from typing import List, Dict, Union
from django.db.models import QuerySet
from catalog.models import Product
from abc import ABC, abstractmethod


class ICatalogRepository(ABC):

    @abstractmethod
    def get_products_by_category(self, category_id: int) -> QuerySet[Product]:
        """Сортировка товаров по категориям."""
        pass

    @abstractmethod
    def get_all_products(self) -> QuerySet[Product]:
        """Все продукты"""
        pass

    @abstractmethod
    def filter_products(self, filters: Dict[str, Union[str, float, List[int]]]) -> QuerySet[Product]:
        """Фильтр продуктов"""
        pass
