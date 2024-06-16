from abc import abstractmethod, ABC
from typing import Optional

from django.core.handlers.wsgi import WSGIRequest
from django.db.models import QuerySet


class IComparisonList(ABC):
    """Интерфейс взаимодействия с данными списка сравнения"""

    @abstractmethod
    def get_comparison_list(self, request: WSGIRequest) -> list[Optional[int]]:
        """Получить список сравнения"""
        pass

    def get_comparison_list_objects(self, request: WSGIRequest) -> Optional[QuerySet]:
        """Получить QuerySet объектов из списка сравнения"""
        pass

    @abstractmethod
    def clear_comparison_list(self, request: WSGIRequest) -> bool:
        """Очистить список сравнения"""
        pass

    @abstractmethod
    def add_to_comparison_list(self, request: WSGIRequest, product_id: int) -> list[int]:
        """Добавить id продукта в список сравнения"""
        pass

    @abstractmethod
    def remove_from_comparison_list(self, request: WSGIRequest, product_id: int) -> list[int]:
        """Убрать id продукта из списка сравнения"""
        pass
