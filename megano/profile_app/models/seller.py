from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from coreapp.models.basemodel import BaseModel


def seller_images_directory_path(instance: 'Seller', filename: str) -> str:
    return f'profile/{instance.user.email}/logo/{filename}'


class Seller(BaseModel):
    """
    Модель профиля продавца
    """

    def __str__(self):
        return f'Модель профиля для продавца {self.user}'

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='seller')
    name = models.CharField(_('Name'), unique=True, max_length=20, blank=False)
    logo = models.ImageField(
        _('Logotype'),
        upload_to=seller_images_directory_path,
        blank=True
    )
    description = models.TextField(_('Description'), blank=True)
