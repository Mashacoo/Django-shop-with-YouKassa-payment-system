from django.contrib.auth.forms import AuthenticationForm
import inject
from auth_app.interfaces.auth_interface import IAuth


class UserAuthenticationForm(AuthenticationForm):

    _user: IAuth = inject.attr(IAuth)

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        if username is not None and password:
            user = self._user.get_user_by_email(username)
            if user is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data
