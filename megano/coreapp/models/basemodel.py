from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):

    """Модель Базовая"""
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('creation time'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('updated time'))
    is_active = models.BooleanField(default=True, verbose_name=_('active'))

    class Meta:
        abstract = True
