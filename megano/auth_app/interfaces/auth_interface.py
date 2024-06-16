from abc import abstractmethod

from auth_app.models.user import User


class IAuth:

    @abstractmethod
    def save(self, model: User) -> None:
        """Сохранить пользователя."""
        pass

    @abstractmethod
    def get_user(self, pk: int):
        """Получаем пользователя"""
        pass

    @abstractmethod
    def get_user_by_email(self, _email: str):
        """Получаем пользователя"""
        pass

    @abstractmethod
    def delete_user_by_email(self, _email: str):
        """Удаление пользователя по email"""
        pass

    @abstractmethod
    def get_user_by_activation_key(self, _activation_key: str):
        """Получаем пользователя по активационному ключу"""
        pass
