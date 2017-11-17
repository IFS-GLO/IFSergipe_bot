from django.conf.urls import url

from bot.chat.telegram.views import TelegramWebhookView

urlpatterns = [
    url('^$', TelegramWebhookView.as_view(), name='telegram_webhook'),
]