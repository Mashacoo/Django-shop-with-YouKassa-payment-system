from abc import abstractmethod


class IDiscounts:

    @abstractmethod
    def get_all_active_cart_discounts(self):
        """Получить все активные скидки типа "Скидки на корзину"""
        pass

    @abstractmethod
    def get_cartitems_by_user_id(self, user_id):
        """ Получить все товары в корзине пользователя по его id"""
        pass

    @abstractmethod
    def get_prices_by_group_of_products_ids(self, ids: list):
        """Получить цены на группу товаров по их id """
        pass

    @abstractmethod
    def get_all_active_product_discounts(self):
        """Получить все активные скидки типа "Скидки на товары" """
        pass

    @abstractmethod
    def get_all_active_set_discounts(self):
        """Получить все активные скидки типа "Скидка на набор" """
        pass
