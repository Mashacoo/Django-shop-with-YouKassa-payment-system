from abc import abstractmethod



class ICore:

    @abstractmethod
    def get_banners(self):
        """Получить все активные баннеры"""
        pass
