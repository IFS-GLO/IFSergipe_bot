from django.conf.urls import url

from .views import BotView

urlpatterns = [
    url('^', BotView.as_view(), name='bot_view')
]
