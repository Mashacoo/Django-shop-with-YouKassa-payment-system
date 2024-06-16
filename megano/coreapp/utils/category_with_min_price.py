import inject
from catalog.interfaces.category_interface import ICategory
from catalog.models import Product, Price
from catalog.interfaces.product_interface import IProduct
from discounts_app.interfaces.discounts_interface import IDiscounts



class CategoryDisplay:

    _category: ICategory = inject.attr(ICategory)
    _product: IProduct = inject.attr(IProduct)
    _discounts: IDiscounts = inject.attr(IDiscounts)

    @classmethod
    def cat_with_min_price(cls, q_cat):
        cat = cls._category.get_categories_to_display()[:q_cat]
        categories = []

        for category in cat:
            cat_new = {}
            cat_new["pk"] = category.pk
            cat_new["title"] = category.title
            cat_new["image"] = category.image
            cat_products = cls._product.get_products_from_lst_categories(cat_pk=category.pk)
            product_pks = list(cat_products.values_list("pk", flat=True))
            prices = cls._discounts.get_prices_by_group_of_products_ids(ids=product_pks)
            price_list_ct = []
            for price in prices:
                price_list_ct.append(price["price"])
            cat_new["price"] = round(min(price_list_ct), 0)
            categories.append(cat_new)

        return categories
