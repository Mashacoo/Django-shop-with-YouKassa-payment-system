import inject
from auth_app.interfaces.auth_interface import IAuth
from django.views import View
from django.shortcuts import redirect, render
from django.http import HttpRequest
from auth_app.utils import send_email_for_verify, get_activation_key
from datetime import date


class ResendActivationKey(View):

    _user: IAuth = inject.attr(IAuth)

    def get(self, request: HttpRequest, activation_key: str):
        return render(request=request, template_name='auth_app/registration_activation_key_expires.html')

    def post(self, request: HttpRequest, activation_key: str):
        user = self._user.get_user_by_activation_key(activation_key)
        user.activation_key = get_activation_key(user.email)
        user.activation_key_will_expires = date.today()
        self._user.save(user)
        send_email_for_verify(request, user)
        return redirect('confirm_email/')
