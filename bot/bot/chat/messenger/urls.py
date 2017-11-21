from django.conf.urls import url

from .views import MessengerWebhookView

urlpatterns = [
    url('^$', MessengerWebhookView.as_view(), name='messenger_webhook'),
]