import inject
from django.core.handlers.wsgi import WSGIRequest
from django.views import generic

from catalog.interfaces.comparison_list_interface import IComparisonList
from services.add_products_to_cart import AddProductsToCart


class ComparisonListView(generic.ListView):
    """Представление для отображения страницы сравнения товаров"""
    template_name = "catalog/comparison.html"
    context_object_name = "comparison_list"

    __comparison_list: IComparisonList = inject.attr(IComparisonList)

    def get_queryset(self, *args, **kwargs):
        """Метод получения набора объектов для отображения"""
        return self.__comparison_list.get_comparison_list_objects(request=self.request)

    def get(self, request, **kwargs):
        """Метод обработки GET запросов"""
        return super().get(request, **kwargs)

    def post(self, request: WSGIRequest, **kwargs):
        """Метод обработки POST запросов"""
        product_id, seller_id, num_products = None, None, None
        try:
            product_id = int(request.POST.get('product_id'))
            seller_id = int(request.POST.get('seller_id'))
            num_products = int(request.POST.get('num_products'))
        except (ValueError, TypeError):
            pass

        if all([seller_id, product_id, num_products]):
            AddProductsToCart(user=request.user)(
                quantity=num_products,
                product_id=product_id,
                seller_id=seller_id
            )
        elif product_id:
            self.__comparison_list.remove_from_comparison_list(request, product_id)

        return self.get(request, **kwargs)
