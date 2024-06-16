from django.contrib import admin
from .models import Cart, CartItem
from services.calculating_total_amount_cart_in_admin_panel import CalculatingTotalAmountCart


class CartItemInline(admin.TabularInline):
    """Отображение и редактирование экземпляров
    модели CartItem в интерфейсе модели Cart в админке"""
    model = CartItem


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    """Регистрация модели Cart в админке"""
    readonly_fields = 'total_amount',
    inlines = [CartItemInline]
    ordering = ["user"]

    @staticmethod
    def total_amount(obj):
        """Динамический расчёт общей стоимости корзины по актуальной цене продукта"""
        return CalculatingTotalAmountCart(cart=obj)()


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    """Регистрация модели CartItem в админке"""
    ordering = ["cart"]
