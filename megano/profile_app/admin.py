from django.contrib import admin
from .models import Profile
from .models import Seller


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    fields = 'avatar', 'phone'
    list_display = 'pk', 'avatar', 'user', 'user_username', 'phone'

    ordering = ('pk',)

    def user_username(self, obj):
        return obj.user.username


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    ordering = 'name',

    def get_queryset(self, request):
        """Возвращает набор экземпляров модели Seller в зависимости от прав пользователя"""
        queryset = super().get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return queryset.filter(user=request.user)

    def get_readonly_fields(self, request, obj=None):
        """Изменяет поля только для просмотра в зависимости от прав пользователя"""
        if request.user.is_superuser:
            return self.readonly_fields
        else:
            return ('user',)
