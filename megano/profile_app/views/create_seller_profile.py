from django.urls import reverse
from django.views.generic import CreateView
from profile_app.forms import SellerForm


class SellerCreateView(CreateView):
    template_name = 'profile_app/create_seller_profile.html'
    form_class = SellerForm

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        user.is_staff = True
        user.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('profile_app:seller_profile', kwargs={'pk': self.object.pk})
