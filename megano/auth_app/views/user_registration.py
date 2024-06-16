from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.views.generic import FormView
from auth_app.models import User
from auth_app.utils import send_email_for_verify
from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from auth_app.forms import UserRegisterForm


class UserRegisterView(UserPassesTestMixin, FormView):

    """
    View функция регистрации пользователя
    """

    def viewing_ban_authenticated_user(self):
        if self.request.user.is_authenticated:
            raise PermissionDenied
        return True

    def get_test_func(self):
        return self.viewing_ban_authenticated_user

    model = User
    template_name = 'auth_app/registration.html'
    form_class = UserRegisterForm

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpRequest:
        form = self.form_class(data=request.POST)
        if form.is_valid():
            user = form.save()
            send_email_for_verify(request, user)
            return redirect('confirm_email/')
        return render(
            request=request,
            template_name=self.template_name,
            context={'form': form}
        )
