from django.urls import path
from .views import ProductDetailView, CatalogPageView, ComparisonListView


app_name = 'catalog'

urlpatterns = [
    path('', CatalogPageView.as_view(template_name='catalog/catalog.html'), name='catalog'),
    path('comparison/', ComparisonListView.as_view(), name='comparison'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
]
