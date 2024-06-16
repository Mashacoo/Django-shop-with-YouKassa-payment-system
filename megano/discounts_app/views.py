from django.shortcuts import render
from discounts_app.services.discount_processing import DiscountProcessing


def get_discount(request):
    res = DiscountProcessing.get_cart_sum_with_discounts(user_id=1)
    return render(request, 'discounts_app/discounts.html', context={'result': res})
