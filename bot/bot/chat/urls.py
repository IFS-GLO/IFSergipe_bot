from django.conf.urls import url

from .views import *

urlpatterns = [
    url('^messenger/', MessengerWebhookView.as_view(), name='messenger_webhook'),
    url('^telegram/', TelegramWebhookView.as_view(), name='telegram_webhook'),
]
