from django.contrib import admin

from coreapp.models.banner import Banner
from coreapp.models.setting import Setting


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
   pass


@admin.register(Setting)
class SettingAdmin(admin.ModelAdmin):
    pass
