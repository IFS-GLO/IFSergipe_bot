from django.conf.urls import url, include

urlpatterns = [
    url(r'^bot/chat/', include('bot.chat.urls', namespace='bot')),
]
