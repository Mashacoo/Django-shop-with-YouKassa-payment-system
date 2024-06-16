import inject
from django.views import View
from django.shortcuts import redirect
from django.http import HttpRequest
from auth_app.interfaces.auth_interface import IAuth
from django.contrib.auth import login
from datetime import date, timedelta


class EmailVerify(View):
    """
    View функция отображения страницы завершения регистрации
    """
    _user: IAuth = inject.attr(IAuth)

    def get(self, request: HttpRequest, activation_key: str):
        user = self._user.get_user_by_activation_key(activation_key)
        if user:
            if user.activation_key_will_expires > date.today() + timedelta(2):
                return redirect('activation_key_expires/')

            user.is_active = True
            self._user.save(user)
            login(request, user)
            return redirect('auth_app:login')
        return redirect('/auth/registration/invalid_verify/')
