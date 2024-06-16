import os
import var_dump as var_dump
from yookassa import Webhook
from yookassa.domain.notification import WebhookNotificationEventType
from megano.settings import WEBHOOKS_URL

whUrl = WEBHOOKS_URL

needWebhookList = [
    WebhookNotificationEventType.PAYMENT_SUCCEEDED,
    WebhookNotificationEventType.PAYMENT_CANCELED
]

whList = Webhook.list()

for event in needWebhookList:
    hookIsSet = False
    for wh in whList.items:
        if wh.event != event:
            continue
        if wh.url != whUrl:
            Webhook.remove(wh.id)
        else:
            hookIsSet = True

    if not hookIsSet:
        Webhook.add({"event": event, "url": whUrl})

var_dump.var_dump(Webhook.list())
