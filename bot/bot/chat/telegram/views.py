import json
from pprint import pprint

import telegram

from django.views import generic
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from telegram.ext import Updater

from bot.chat.telegram.handlers import send_message
from bot.settings import TELEGRAM_ACCESS_TOKEN, WEBHOOK
from bot.chat.models import *

bot_model = Bot

telegram_bot = telegram.Bot(token=TELEGRAM_ACCESS_TOKEN)
telegram_bot.setWebhook(WEBHOOK)

updater = Updater(token=TELEGRAM_ACCESS_TOKEN)
dispatcher = updater.dispatcher

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
                    chat = Chat(id=int(chat['id']), username=chat['username'], first_name=chat['first_name'], last_name=chat['last_name']).save()

            message = incoming_message['message'].get('text')  # get the input msg

            # Check if message is a command
            if message[0] == '/':
                command = Command.objects.filter(trigger=message.split()[0].lower())  # check if command exist in list

                # if command exist
                if command:
                    response = send_message(telegram_bot, chat, message)

                    update = ChatUpdate()
                    update.command = message
                    update.chat = Chat.objects.get(id=chat['id'])
                    update.save()

                else:
                    send_message(telegram_bot, chat, 'unknow')

        return HttpResponse()
