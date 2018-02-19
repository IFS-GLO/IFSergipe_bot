import json
from pprint import pprint

import telegram

from django.views import generic
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from telegram.ext import Updater

from bot.chat.telegram.handlers import commands
from bot.settings import TELEGRAM_ACCESS_TOKEN, WEBHOOK
from bot.chat.models import *

bot_model = Bot

telegram_bot = telegram.Bot(token=TELEGRAM_ACCESS_TOKEN)
telegram_bot.setWebhook(WEBHOOK)

updater = Updater(token=TELEGRAM_ACCESS_TOKEN)
dispatcher = updater.dispatcher

# TODO: Armazenar informações do chat no banco de dados
# para gerenciamento das atividades, assim um chat
# não sobrescreverá informações de outro

class TelegramWebhookView(generic.View):

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return generic.View.dispatch(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        incoming_message = json.loads(request.body.decode('utf-8'))

        if incoming_message['message']:
            chat = incoming_message['message']['chat']

            # check if bot is running
            if Chat.objects.filter(is_running=True):
                pass

            else:
                # check if chat exist
                if Chat.objects.filter(id=int(chat['id'])).exists() is False:
                    chat = Chat(id=int(chat['id']), username=chat['username'], first_name=chat['first_name'], last_name=chat['last_name'], is_running=True).save()

            message = incoming_message['message'].get('text')  # get the input msg
            command = Command.objects.filter(trigger=message)[0]

            # if command exist
            if command:
                text = command.message

                # check if exist arguments
                if command.arguments is not '':
                    # TODO: a function to check if exist more than one arg
                    text = text.format(chat[command.arguments])

                telegram_bot.send_message(
                    parse_mode='Markdown',
                    chat_id=chat['id'],
                    text=text,
                )

            else: # if not exist send a msg to user
                text = 'Comando não localizado.'
                telegram_bot.send_message(
                    parse_mode='Markdown',
                    chat_id=chat['id'],
                    text=text,
                )

        return HttpResponse()
