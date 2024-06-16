from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpRequest
from django.template.loader import render_to_string
from auth_app.models import User


def send_email_for_verify(request: HttpRequest, user: User) -> None:
    """
    Функция отправки письма пользователю со ссылкой для подтверждения регистрации
    """

    current_site = get_current_site(request)
    context = {
        'user': user,
        'domain': current_site.domain,
        'activation_key': user.activation_key,
    }
    message = render_to_string(
        'auth_app/registration_verify_email.html',
        context=context,
    )
    email = EmailMessage(
        'Veryfi email',
        message,
        to=[user.email],
    )
    email.send()
