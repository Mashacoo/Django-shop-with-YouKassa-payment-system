import inject

from auth_app.models.user import User
from catalog.interfaces.product_interface import IProduct
from catalog.interfaces.review_interface import IReview
from catalog.models import Review


class AddReview:
    """Класс для реализации методов добавления отзывов к продукту"""
    __product: IProduct = inject.attr(IProduct)
    __review: IReview = inject.attr(IReview)

    def __init__(self, user: User):
        self.user = user

    def __call__(self, product_id: int, review: str) -> None:
        """Метод добавления отзыва к продукту"""
        self.__review.save(
            Review(
                product=self.__product.get_product(pk=product_id),
                author=self.user,
                review=review
            )
        )
