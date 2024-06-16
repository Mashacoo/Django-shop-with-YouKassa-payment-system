from django.contrib.auth.forms import UserCreationForm
from auth_app.models import User
from django.utils.translation import gettext_lazy as _
from django import forms
from auth_app.utils import get_activation_key


class UserRegisterForm(UserCreationForm):
    """
    Форма регистрации нового пользователя
    """

    error_messages = {
        "password_mismatch": _("Пароли не совпадают! Введите пароль заново"),
    }

    email = forms.EmailField(
        label='Адрес эл.почты',
        widget=forms.EmailInput(
            attrs={'placeholder': 'Введите адрес эл.почты'}
        )
    )

    password1 = forms.CharField(
        label='Введите пароль',
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Введите пароль'}
        )
    )
    password2 = forms.CharField(
        label='Подтвердите пароль',
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Повторите пароль'}
        )
    )

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(UserRegisterForm, self).save()
        user.is_active = False
        user.activation_key = get_activation_key(user.email)
        user.save()
        return user
