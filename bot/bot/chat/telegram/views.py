import json
import telegram

from django.views import generic
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from bot.settings import TELEGRAM_ACCESS_TOKEN

telegram_bot = telegram.Bot(token=TELEGRAM_ACCESS_TOKEN)


class TelegramWebhookView(generic.View):
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return generic.View.dispatch(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        incoming_message = json.loads(request.body.decode('utf-8'))

        # TODO: Create message Model
        if incoming_message['message']:
            # message = incoming_message['message']
            chat_id = incoming_message['message']['chat']['id']
            message = incoming_message['message'].get('text')

            telegram_bot.send_message(chat_id=chat_id, text=message)

            """command = commands.get(message.split()[0].lower())  # check if command exist in list
            if command:
                command(incoming_message['message']['chat'])"""

            # pprint(json.loads(request.body.decode('utf-8')))

        return HttpResponse()
