import json

from django.http.response import HttpResponse
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from wit import Wit

from bot.chat.messenger.bot import Bot
from bot.settings import SECRET_KEY, WIT_ACCESS_TOKEN

wit_client = Wit(access_token=WIT_ACCESS_TOKEN)


class MessengerWebhookView(generic.View):
    def get(self, request, *args, **kwargs):
        if self.request.GET.get(u'hub.verify_token') == SECRET_KEY:
            return HttpResponse(self.request.GET['hub.challenge'])
        else:
            return HttpResponse('Error, invalid token')

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return generic.View.dispatch(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        incoming_message = json.loads(self.request.body.decode('utf-8'))

        for entry in incoming_message['entry']:
            for message in entry['messaging']:
                if 'message' in message:
                    Bot.run_actions(wit_client, message)

        return HttpResponse()
