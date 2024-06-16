from random import random
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def base_view(request: HttpRequest) -> HttpResponse:
    return render(request, "coreapp/base.html")
