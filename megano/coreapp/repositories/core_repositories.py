from beartype import beartype
from coreapp.interfaces.core_interface import ICore
from coreapp.models.banner import Banner


class CoreRepository(ICore):
    @beartype
    def get_banners(self):
        return Banner.objects.all().filter(is_active=True)
