from beartype import beartype
from catalog.interfaces.category_interface import ICategory
from catalog.models import Category


class CategoryRepository(ICategory):

    @beartype
    def get_categories_to_display(self):
        return Category.objects.filter(display_on_index_page=True)
