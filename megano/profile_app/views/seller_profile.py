import inject
from django.views.generic import DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from profile_app.interfaces import ISeller
from catalog.models import Product


class SellerProfileView(DetailView):

    def get_template_names(self):
        if self.request.resolver_match.kwargs['pk'] == self.request.user.seller.pk:
            return 'profile_app/seller_profile.html'
        return 'profile_app/seller_profile_for_average_user.html'

    context_object_name = 'seller'
    paginate_by = 4
    _seller: ISeller = inject.attr(ISeller)

    def get_object(self, *args, **kwargs):
        return self._seller.get_seller(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = Product.objects.filter(prices__seller=self.kwargs['pk']).prefetch_related('prices', 'product_images')
        paginator = Paginator(products, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            products_page = paginator.page(page)
        except PageNotAnInteger:
            products_page = paginator.page(1)
        except EmptyPage:
            products_page = paginator.page(paginator.num_pages)

        context['products_page'] = products_page
        return context
