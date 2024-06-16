from abc import abstractmethod, ABC

from catalog.models import Review


class IReview(ABC):
    """Интерфейс взаимодействия с данными модели Review"""

    @abstractmethod
    def save(self, model: Review) -> None:
        """Сохранить экземпляр модели RecentlyViewedProducts"""
        pass
