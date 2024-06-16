from typing import Optional

import inject
from beartype import beartype
from django.conf import settings
from django.core.handlers.wsgi import WSGIRequest
from django.db.models import QuerySet

from catalog.interfaces.comparison_list_interface import IComparisonList
from catalog.interfaces.product_interface import IProduct


class ComparisonListRepository(IComparisonList):
    """Для реализации методов взаимодействия с данными
    списка сравнения на основании интерфейса IComparisonList"""
    __product: IProduct = inject.attr(IProduct)

    @beartype
    def get_comparison_list(self, request: WSGIRequest) -> list[Optional[int]]:
        """Получить список сравнения"""
        comparison_list = request.session.get('comparison_list')
        if not comparison_list:
            comparison_list = []
            request.session['comparison_list'] = comparison_list
        return comparison_list

    @beartype
    def get_comparison_list_objects(self, request: WSGIRequest) -> Optional[QuerySet]:
        """Получить QuerySet объектов из списка сравнения"""
        if comparison_list := self.get_comparison_list(request):
            return self.__product.get_products_for_comparison_list(list_pk=comparison_list)

    @beartype
    def clear_comparison_list(self, request: WSGIRequest) -> bool:
        """Очистить список сравнения"""
        comparison_list = self.get_comparison_list(request)
        comparison_list.clear()
        request.session['comparison_list'] = comparison_list
        return not comparison_list

    @beartype
    def add_to_comparison_list(self, request: WSGIRequest, product_id: int) -> list[int]:
        """Добавить id продукта в список сравнения"""
        comparison_list = self.get_comparison_list(request)
        if product_id not in comparison_list:
            comparison_list.append(product_id)
        request.session['comparison_list'] = comparison_list[
                                             -settings.DEFAULT_NUM_PRODUCTS_IN_COMPARISON_LIST:]
        return comparison_list

    @beartype
    def remove_from_comparison_list(self, request: WSGIRequest, product_id: int) -> list[int]:
        """Убрать id продукта из списка сравнения"""
        comparison_list = self.get_comparison_list(request)
        try:
            comparison_list.remove(product_id)
        except ValueError:
            pass
        request.session['comparison_list'] = comparison_list
        return comparison_list
