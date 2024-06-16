from django.db import models
from coreapp.models.basemodel import BaseModel
from coreapp.utils.images_directory_path import banner_images_directory_path


class Banner (BaseModel):

    """Модель Баннера на главной странице """

    class Meta:
        verbose_name = 'Banner'
        verbose_name_plural = 'Banners'

    title1 = models.CharField(max_length=30, null=True, blank=True, verbose_name='banner_title1')
    title2 = models.CharField(max_length=30, null=True, blank=True, verbose_name='banner_title2')
    title3 = models.CharField(max_length=30, null=True, blank=True, verbose_name='banner_title3')
    text = models.TextField(max_length=200, null=True, blank=True, verbose_name='banner_text')
    button = models.CharField(max_length=30, null=True, blank=True, default="Get Started", verbose_name='banner_footer')
    image = models.ImageField(upload_to=banner_images_directory_path, null=True, blank=True, verbose_name='banner_image')
    link = models.URLField(null=True, blank=True, verbose_name='banner_link')
