from django import forms
from catalog.models import Seller, Category


class ProductFilterForm(forms.Form):
    title = forms.CharField(label='Название', required=False)
    price_min = forms.FloatField(label='Цена от', required=False)
    price_max = forms.FloatField(label='Цена до', required=False)
    available = forms.ChoiceField(choices=[('', 'Не учитывать'), ('True', 'Да'), ('False', 'Нет')],
                                  label='Только товары в наличии', required=False)
    free_delivery = forms.ChoiceField(choices=[('', 'Не учитывать'), ('True', 'Да'), ('False', 'Нет')],
                                      label='С бесплатной доставкой', required=False)
    seller = forms.ModelMultipleChoiceField(queryset=Seller.objects.all(), widget=forms.CheckboxSelectMultiple,
                                            required=False)
    is_limited = forms.ChoiceField(choices=[('', 'Не учитывать'), ('True', 'Да'), ('False', 'Нет')],
                                   label='Ограниченный товар', required=False)
    tag = forms.CharField(label='Тег', required=False)
    category = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), widget=forms.CheckboxSelectMultiple,
                                              required=False)
    sort = forms.ChoiceField(choices=[
        ('', 'Не учитывать'),
        ('price', 'Цена (по возрастанию)'),
        ('-price', 'Цена (по убыванию)'),
        ('popularity', 'Популярность (по убыванию)'),
        ('-created_at', 'Новизне (по убыванию)'),
    ], label='Сортировать по', required=False)


class PriceModelAdminForm(forms.ModelForm):
    """Форма для создания модели Price админке с ограничением выбора
    поля seller в зависимости от прав пользователя"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.user.is_superuser:
            self.fields['seller'].queryset = self.fields['seller'].queryset.filter(user=self.user)
