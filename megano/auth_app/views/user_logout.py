from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy


class UserLogoutView(LogoutView):
    """
        View функция выхода из учетной записи пользователя
    """
    next_page = reverse_lazy('auth_app:login')
