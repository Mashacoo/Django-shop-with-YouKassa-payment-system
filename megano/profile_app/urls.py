from django.urls import path
from .views import (
    ProfileView,
    ProfileChangeView,
    SellerCreateView,
    SellerProfileView,
    SellerProfileChangeView
)

app_name = 'profile_app'

urlpatterns = [
    path('<int:pk>/', ProfileView.as_view(), name='profile'),
    path('<int:pk>/change_profile/', ProfileChangeView.as_view(), name='change_profile'),
    path('create_seller/', SellerCreateView.as_view(), name='create_seller_profile'),
    path('seller/<int:pk>/', SellerProfileView.as_view(), name='seller_profile'),
    path('seller/<int:pk>/change_seller/', SellerProfileChangeView.as_view(), name='change_seller_profile'),
]

