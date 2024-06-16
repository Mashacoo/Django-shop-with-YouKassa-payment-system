import inject
from django.contrib.auth.views import LoginView
from django.contrib.auth import login as auth_login
from profile_app.interfaces import IProfile
from auth_app.utils import add_to_cart_from_session_cart
from django.http import HttpResponseRedirect


class UserLoginView(LoginView):
    """
    View функция отображения страницы логирования на сайт
    """
    _profile: IProfile = inject.attr(IProfile)
    template_name = 'auth_app/login.html'
    redirect_authenticated_user = True

    def form_valid(self, form):
        """Security check complete. Log the user in."""
        auth_login(self.request, form.get_user())
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        if self.request.session.get('cart'):
            add_to_cart_from_session_cart(self.request)
        profile = self._profile.get_profile_by_user_id(self.request.user.pk)
        return f'/profile/{profile.pk}/'
