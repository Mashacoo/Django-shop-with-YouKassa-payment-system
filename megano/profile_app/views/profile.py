import inject
from profile_app.models import Profile
from django.views.generic import DetailView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from order_app.interface import IOrder


class ProfileView(UserPassesTestMixin, DetailView):

    def ban_viewing_another_profiles(self):
        if self.request.resolver_match.kwargs['pk'] != self.request.user.profile.pk:
            raise PermissionDenied
        return True

    def get_test_func(self):
        return self.ban_viewing_another_profiles

    template_name = 'profile_app/profile.html'
    model = Profile
    context_object_name = 'profile'
    paginate_by = 2
    _order: IOrder = inject.attr(IOrder)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_orders = self._order.get_all_users_orders(self.request.user)
        paginator = Paginator(user_orders, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            products_page = paginator.page(page)
        except PageNotAnInteger:
            products_page = paginator.page(1)
        except EmptyPage:
            products_page = paginator.page(paginator.num_pages)

        context['user_order_pages'] = products_page
        return context
