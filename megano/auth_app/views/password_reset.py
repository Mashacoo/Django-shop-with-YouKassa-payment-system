from django.contrib.auth.views import PasswordResetConfirmView
from django.urls import reverse_lazy


class UserPasswordConfirmView(PasswordResetConfirmView):
    template_name = 'auth_app/password_reset.html'
    success_url = reverse_lazy('auth_app:confirm_reset_password')
