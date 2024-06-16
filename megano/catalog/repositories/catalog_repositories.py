from django.db.models import QuerySet
from beartype import beartype
from catalog.interfaces.catalog_interface import ICatalogRepository
from catalog.models import Product
from catalog.utils.filter_utils import filter_products
from django.db.models import Min


class CatalogRepository(ICatalogRepository):

    @beartype
    def get_products_by_category(self, category_id: int) -> QuerySet[Product]:
        if category_id is not None:
            return Product.objects.filter(category__id=category_id)
        return Product.objects.all()

    @beartype
    def get_all_products(self) -> QuerySet[Product]:
        return Product.objects.all()

    @beartype
    def filter_products(self, **filters) -> QuerySet[Product]:

        products = self.get_all_products()
        products = filter_products(products, filters)

        return products.annotate(prices__price__min=Min('prices__price'))
