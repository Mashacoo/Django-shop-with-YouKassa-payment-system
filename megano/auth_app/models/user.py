from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db import models
from .usermanager import NewUserManager


class User(AbstractUser):
    """
    Новая модель пользователя
    """

    def __str__(self):
        return f'Модель для пользователя {self.email}'

    username = models.CharField(
        _('username'),
        max_length=150,
        unique=False,
        blank=True
    )

    email = models.EmailField(
        _('email'),
        max_length=60,
        unique=True,
        error_messages={
            "unique": _("Пользователь с таким email уже существует"),
        }
    )

    activation_key = models.CharField(
        max_length=60,
        blank=True
    )

    activation_name_set = models.CharField(
        max_length=60,
        blank=True
    )

    activation_key_will_expires = models.DateField(
        _("date of creation activation key"),
        auto_now_add=True
    )

    objects = NewUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
