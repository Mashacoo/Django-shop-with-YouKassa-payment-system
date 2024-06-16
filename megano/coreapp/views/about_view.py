from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def about_view(request: HttpRequest) -> HttpResponse:
    return render(request, "coreapp/about.html")
