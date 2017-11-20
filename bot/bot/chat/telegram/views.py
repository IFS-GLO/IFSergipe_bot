import json
from pprint import pprint

import telegram

from django.views import generic
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from telegram.ext import Updater

from bot.chat.telegram.handlers import commands
from bot.settings import TELEGRAM_ACCESS_TOKEN
from bot.chat.models import Bot

bot_model = Bot

telegram_bot = telegram.Bot(token=TELEGRAM_ACCESS_TOKEN)
telegram_bot.setWebhook(
    'https://api.telegram.org/bot451087671:AAEpKcBxN6qx3z4PNs61f6PChlGpBzWc52Y/setWebhook?'
    'url=https://08d260a0.ngrok.io/bot/chat/telegram/'
)

updater = Updater(token=TELEGRAM_ACCESS_TOKEN)
dispatcher = updater.dispatcher

# TODO: Armazenar informações do chat no banco de dados
# para gerenciamento das atividades, assim um chat
# não sobrescreverá informações de outro

class TelegramWebhookView(generic.View):
    def run_next_command(self, command, chat, message):
        instance = command['next_command'](message)

        if command['template']:
            bot_model.running = command['template'](telegram_bot, chat, instance)

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return generic.View.dispatch(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        incoming_message = json.loads(request.body.decode('utf-8'))

        # TODO: Create message Model
        if incoming_message['message']:
            chat = incoming_message['message']['chat']
            message = incoming_message['message'].get('text')

            command = commands.get(message.split()[0].lower())  # check if command exist in list

            if bot_model.running:
                self.run_next_command(bot_model.next_command, chat, message)

            if command:
                bot_model.running = True
                bot_model.next_command = command(telegram_bot, chat)

        return HttpResponse()
