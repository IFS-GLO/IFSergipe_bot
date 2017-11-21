from django.conf.urls import url, include

urlpatterns = [
    url('^messenger/', include('bot.chat.messenger.urls', namespace='messenger')),
    url('^telegram/', include('bot.chat.telegram.urls', namespace='telegram')),
]
