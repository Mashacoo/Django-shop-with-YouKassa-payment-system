from django.db import models
from .basemodel import BaseModel


class Setting(BaseModel):
    """Модель для хранения настроек"""
    key = models.CharField(max_length=255, unique=True, verbose_name='key')
    value = models.TextField(verbose_name='value')

    class Meta:
        verbose_name = 'Setting'
        verbose_name_plural = 'Settings'

    def __str__(self):
        return self.key
