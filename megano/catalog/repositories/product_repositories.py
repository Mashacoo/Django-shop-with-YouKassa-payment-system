from typing import Optional

from beartype import beartype
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Min, F, QuerySet

from catalog.interfaces.product_interface import IProduct
from catalog.models import Product


class ProductRepository(IProduct):
    """Для реализации методов взаимодействия с данными
    модели Product на основании интерфейса IProduct"""

    @beartype
    def get_product(self, pk: int) -> Optional[Product]:
        """Получить экземпляр модели Product"""
        try:
            return Product.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return None

    @beartype
    def get_product_with_image(self, pk: int) -> Optional[Product]:
        """Получить экземпляр модели Product с изображениями"""
        try:
            return Product.objects.get(pk=pk).select_related('product_image')
        except ObjectDoesNotExist:
            return None

    @beartype
    def get_product_for_detail_view(self, pk: int) -> Optional[Product]:
        """Получить экземпляр модели Product с необходимыми связями и аннотациями
        для отображения детальной страницы товара"""
        try:
            return Product.objects.annotate(
                min_price=Min('prices__price')).filter(
                prices__price=F('min_price')).annotate(
                min_price_seller_id=F('prices__seller')).prefetch_related(
                'prices', 'product_characteristics', 'product_images', 'reviews').get(pk=pk)
        except ObjectDoesNotExist:
            return None

    @beartype
    def get_products_for_comparison_list(self, list_pk: list) -> QuerySet:
        """Получить набор экземпляров модели Product для сравнения согласно списка list_pk"""
        queryset = Product.objects.annotate(
            min_price=Min('prices__price')).filter(
            prices__price=F('min_price')).annotate(
            min_price_seller_id=F('prices__seller')).prefetch_related(
            'product_images',
            'product_characteristics',
            'product_characteristics__characteristic').filter(pk__in=list_pk)

        common_characteristics = []
        for product in queryset:
            product_characteristics = product.product_characteristics.all().values_list(
                'characteristic__title', flat=True)
            common_characteristics.extend(product_characteristics)

        common_characteristics = [characteristic for characteristic in common_characteristics
                                  if common_characteristics.count(characteristic) > 1]

        for product in queryset:
            if len(common_characteristics) > 1:
                product.common_characteristics = product.product_characteristics.all().values(
                    'characteristic__title', 'value').filter(
                    characteristic__title__in=common_characteristics)
            else:
                product.common_characteristics = product.product_characteristics.all().values(
                    'characteristic__title', 'value')

        return queryset

    @beartype
    def get_limited_products(self):
        return Product.objects.filter(is_limited=True)

    @beartype
    def get_products(self):
        return Product.objects.filter(is_active=True)

    @beartype
    def get_products_from_lst_categories(self, cat_pk):
        return Product.objects.select_related('category').filter(category_id=cat_pk)