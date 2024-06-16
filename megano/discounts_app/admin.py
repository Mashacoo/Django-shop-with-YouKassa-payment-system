from django.contrib import admin
from discounts_app.models.product_set import ProductSet
from discounts_app.models.set_discount import SetDiscount
from discounts_app.models.cart_discount import CartDiscount
from discounts_app.models.product_discount import ProductDiscount


@admin.register(ProductSet)
class ProductSetAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductDiscount)
class ProductDiscountAdmin(admin.ModelAdmin):
    pass


@admin.register(SetDiscount)
class SetDiscountAdmin(admin.ModelAdmin):
    pass


@admin.register(CartDiscount)
class CartDiscountAdmin(admin.ModelAdmin):
    pass
