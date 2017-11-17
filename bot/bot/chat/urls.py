from django.conf.urls import url, include

from .views import *

urlpatterns = [
    url('^messenger/', MessengerWebhookView.as_view(), name='messenger_webhook'),
    url('^telegram/', include('bot.chat.telegram.urls', namespace='telegram')),
]
