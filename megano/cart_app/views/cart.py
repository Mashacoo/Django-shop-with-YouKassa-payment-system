from django.views.generic import TemplateView
from discounts_app.services.discount_processing import DiscountProcessing


class CartView(TemplateView):
    """Отображение корзины пользователя"""
    template_name = "cart_app/cart.html"
    context_object_name = 'cart'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        sale_price = DiscountProcessing.get_cart_sum_with_discounts(self.request.user.pk)
        context['sale_price'] = sale_price
        return context
