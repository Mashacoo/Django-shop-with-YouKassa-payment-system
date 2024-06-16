from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from coreapp.models.basemodel import BaseModel


def profile_images_directory_path(instance: 'Profile', filename: str) -> str:
    return f'profile/{instance.user.email}/avatars/{filename}'


class Profile(BaseModel):
    """
    Модель профиля пользователя
    """

    def __str__(self):
        return f'Модель профиля для пользователя {self.user.email}'

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    phone = models.CharField(_('phone number'), max_length=10, blank=True)
    avatar = models.ImageField(
        _('profile avatar'),
        upload_to=profile_images_directory_path,
        blank=True
    )
