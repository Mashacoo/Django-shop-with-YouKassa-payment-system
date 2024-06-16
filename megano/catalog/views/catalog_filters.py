import inject
from django.core.handlers.wsgi import WSGIRequest
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Min
from django.views.generic import ListView

from catalog.interfaces.comparison_list_interface import IComparisonList
from catalog.models import Product
from catalog.interfaces.catalog_interface import ICatalogRepository
from catalog.utils import add_product_from_catalog


class CatalogPageView(ListView):
    template_name = 'catalog/catalog'
    _catalog_repository: ICatalogRepository = inject.attr(ICatalogRepository)
    paginate_by = 9
    __comparison_list: IComparisonList = inject.attr(IComparisonList)
    show_buy_modal = False

    def get_queryset(self):
        return self._get_filtered_and_sorted_products()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = self._get_filtered_and_sorted_products()
        context['products'] = products

        paginator = Paginator(products, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            products_page = paginator.page(page)
        except PageNotAnInteger:
            products_page = paginator.page(1)
        except EmptyPage:
            products_page = paginator.page(paginator.num_pages)

        context['products_page'] = products_page
        context['show_buy_modal'] = self.show_buy_modal
        self.show_buy_modal = False
        return context

    def _get_filtered_and_sorted_products(self):
        try:
            filters = {
                'category_id': self.request.GET.get('category_id'),
                'title': self.request.GET.get('title'),
                'available': self.request.GET.get('available'),
                'free_delivery': self.request.GET.get('free_delivery'),
                'is_limited': self.request.GET.get('is_limited'),
                'tag': self.request.GET.get('tag'),
                'category': self.request.GET.getlist('category'),
            }

            price_range = self.request.GET.get('price')
            if price_range:
                price_min, price_max = map(float, price_range.split(';'))
                filters['price_min'] = price_min
                filters['price_max'] = price_max

            products = self._catalog_repository.filter_products(**filters)

            sort = self.request.GET.get('sort')
            if sort == 'price':
                sort_direction = self.request.GET.get('sort_direction', 'asc')

                sort_field = f'prices__price__min{"-" if sort_direction == "desc" else ""}'
                products = products.annotate(prices__price__min=Min('prices__price')).order_by(sort_field)
            elif sort == 'popularity':
                products = products.order_by('-views')
            elif sort == 'reviews':
                products = products.order_by('-reviews')
            elif sort == 'newness':
                products = products.order_by('-created_at')

            return products
        except KeyError:
            return Product.objects.none()


    def get(self, request, **kwargs):
        """Метод для обработки GET запросов"""
        return super().get(request, **kwargs)

    def post(self, request: WSGIRequest, **kwargs):
        """Метод для обработки POST запросов"""
        if 'add_product_to_comparison_from_catalog' in request.POST:
            try:
                product_id = int(request.POST.get('product_id'))
            except (ValueError, TypeError) as exc:
                raise exc
            else:
                self.__comparison_list.add_to_comparison_list(request, product_id)
            return self.get(request, **kwargs)
        elif 'add_product_to_cart_from_catalog' in request.POST:
            add_product_from_catalog(
                request=request,
                product_id=int(request.POST.get('product_id')),
                price=request.POST.get('price'))
            self.show_buy_modal = True
            return self.get(request, **kwargs)
