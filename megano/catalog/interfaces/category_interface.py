from abc import abstractmethod


class ICategory:

    @abstractmethod
    def get_categories_to_display(self):
        """Получить все категории товаров с отметкой для отражения на главной странице"""
        pass
