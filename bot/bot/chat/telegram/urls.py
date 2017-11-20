from django.conf.urls import url

from .views import TelegramWebhookView

urlpatterns = [
    url('^$', TelegramWebhookView.as_view(), name='telegram_webhook'),
]