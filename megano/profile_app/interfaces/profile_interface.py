from abc import abstractmethod
from profile_app.models import Profile


class IProfile:

    @abstractmethod
    def save(self, model: Profile) -> None:
        """Сохранить пользователя."""
        pass

    @abstractmethod
    def get_profile_by_user_id(self, _user_id: str):
        """Получаем пользователя"""
        pass

    @abstractmethod
    def delete_profile_by_user_id(self, _user_id: str):
        """Удаление пользователя по email"""
        pass
