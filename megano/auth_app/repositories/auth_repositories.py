from beartype import beartype
from auth_app.interfaces.auth_interface import IAuth
from auth_app.models.user import User
from django.core.exceptions import ObjectDoesNotExist
from typing import Optional


class AuthRepository(IAuth):

    @beartype
    def save(self, model: User) -> None:
        model.save()

    @beartype
    def get_user_by_email(self, _email: str) -> Optional[User]:
        """Получаем пользователя"""
        try:
            return User.objects.get(email=_email)
        except ObjectDoesNotExist:
            return None

    @beartype
    def get_user(self, pk: int) -> Optional[User]:
        """Получаем пользователя"""
        try:
            return User.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return None

    @beartype
    def delete_user_by_email(self, _email: str) -> None:
        """Удаляем пользователя"""
        user = self.get_user_by_email(_email)
        if user:
            user.delete()

    @beartype
    def get_user_by_activation_key(self, _activation_key: str) -> Optional[User]:
        """Получаем пользователя по активационному ключу"""
        try:
            return User.objects.get(activation_key=_activation_key)
        except ObjectDoesNotExist:
            return None

    #
    # @beartype
    # def add_permissions(self, ):
