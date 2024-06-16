import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from yookassa import Configuration, Payment
from yookassa.domain.notification import WebhookNotificationEventType, WebhookNotificationFactory
from order_app.services.confimation_payment import PaymentConfirmation
from megano.settings import PAYMENT_SECRET_KEY,PAYMENT_ACCOUNT_ID


@csrf_exempt
def my_webhook_handler(request):

    # Извлечение JSON объекта из тела запроса
    event_json = json.loads(request.body)
    try:
        # Создание объекта класса уведомлений в зависимости от события
        notification_object = WebhookNotificationFactory().create(event_json)
        response_object = notification_object.object
        print(response_object)
        if notification_object.event == WebhookNotificationEventType.PAYMENT_SUCCEEDED:
            some_data = {
                'paymentId': response_object.id,
                'paymentStatus': response_object.status,
            }

        elif notification_object.event == WebhookNotificationEventType.PAYMENT_WAITING_FOR_CAPTURE:
            some_data = {
                'paymentId': response_object.id,
                'paymentStatus': response_object.status,
            }

        elif notification_object.event == WebhookNotificationEventType.PAYMENT_CANCELED:
            some_data = {
                'paymentId': response_object.id,
                'paymentStatus': response_object.status,
            }

        elif notification_object.event == WebhookNotificationEventType.REFUND_SUCCEEDED:
            some_data = {
                'refundId': response_object.id,
                'refundStatus': response_object.status,
                'paymentId': response_object.payment_id,
            }

        elif notification_object.event == WebhookNotificationEventType.DEAL_CLOSED:
            some_data = {
                'dealId': response_object.id,
                'dealStatus': response_object.status,
            }

        elif notification_object.event == WebhookNotificationEventType.PAYOUT_SUCCEEDED:
            some_data = {
                'payoutId': response_object.id,
                'payoutStatus': response_object.status,
                'dealId': response_object.deal.id,
            }

        elif notification_object.event == WebhookNotificationEventType.PAYOUT_CANCELED:
            some_data = {
                'payoutId': response_object.id,
                'payoutStatus': response_object.status,
                'dealId': response_object.deal.id,
            }

        else:
            # Обработка ошибок
            print("Error in identifying")
            return HttpResponse(status=400)  # Сообщаем кассе об ошибке

        Configuration.configure(PAYMENT_ACCOUNT_ID, PAYMENT_SECRET_KEY)
        # Получим актуальную информацию о платеже
        payment_info = Payment.find_one(some_data['paymentId'])

        if payment_info:
            if PaymentConfirmation.confirm_payment(payment_info):
                return HttpResponse(status=200)
            else:
                print('оплата не прошла')
                return HttpResponse(status=400)  # Сообщаем кассе об ошибке

    except Exception as e:
        print(e, 'ошибка здесь')
        return HttpResponse(status=400)  # Сообщаем кассе об ошибке
