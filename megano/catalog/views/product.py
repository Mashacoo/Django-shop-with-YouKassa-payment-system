import inject
from django.core.handlers.wsgi import WSGIRequest
from django.views import generic
from catalog.interfaces.product_interface import IProduct
from services.add_products_to_cart import AddProductsToCart
from services.add_review import AddReview
from services.recently_viewed_products import RecentlyViewedProductsService
from catalog.utils import add_product_to_session_cart


class ProductDetailView(generic.DetailView):
    """Представление для отображения детальной страницы товара"""
    template_name = "catalog/product.html"
    context_object_name = "product"
    show_buy_modal = False
    show_review_modal = False
    __product: IProduct = inject.attr(IProduct)

    def get_object(self, *args, **kwargs):
        return self.__product.get_product_for_detail_view(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        """Формирует контекст для шаблона"""
        context = super().get_context_data(**kwargs)
        context['show_buy_modal'] = self.show_buy_modal
        context['show_review_modal'] = self.show_review_modal
        self.show_buy_modal = False
        self.show_review_modal = False
        return context

    def get(self, request: WSGIRequest, *args, **kwargs):
        """Метод обработки GET запросов"""
        if request.user.is_authenticated:
            RecentlyViewedProductsService(user=request.user).add(product_id=kwargs['pk'])
        return super().get(request, *args, **kwargs)

    def post(self, request: WSGIRequest, *args, **kwargs):
        """Метод обработки POST запросов"""
        if request.user.is_authenticated:
            if review := request.POST.get('review'):
                self.show_review_modal = True
                AddReview(user=request.user)(
                    product_id=kwargs['pk'],
                    review=review
                )
            else:
                self.show_buy_modal = True
                AddProductsToCart(user=request.user)(
                    quantity=int(request.POST.get('num_products')),
                    product_id=kwargs['pk'],
                    seller_id=int(request.POST.get('seller_id'))
                )
        else:
            self.show_buy_modal = True
            cart = request.session.get('cart', [])
            request.session['cart'] = add_product_to_session_cart(
                cart=cart,
                seller_id=int(request.POST.get('seller_id')),
                product_id=kwargs['pk'],
                num_products=int(request.POST.get('num_products'))
            )
        return self.get(request, *args, **kwargs)
