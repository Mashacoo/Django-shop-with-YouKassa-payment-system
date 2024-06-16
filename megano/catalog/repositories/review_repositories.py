from beartype import beartype
from catalog.interfaces.review_interface import IReview
from catalog.models import Review


class ReviewRepository(IReview):
    """Для реализации методов взаимодействия с данными
    модели Review на основании интерфейса IReview"""

    @beartype
    def save(self, model: Review) -> None:
        """Сохранить экземпляр модели Review"""
        model.save()
