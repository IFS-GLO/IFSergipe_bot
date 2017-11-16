import json
from pprint import pprint

from django.views import generic
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from bot.settings import SECRET_KEY, WIT_ACCESS_TOKEN, TELEGRAM_ACCESS_TOKEN

from wit import Wit
import telegram

from .bot import Bot

wit_client = Wit(access_token=WIT_ACCESS_TOKEN)

telegram_bot = telegram.Bot(token=TELEGRAM_ACCESS_TOKEN)


def start(chat):
    text = 'Opa ' + chat['first_name'] + '!\n'
    text += '\n'

    text += 'Sou um assistente virtual criado para te auxiliar. Escolha um dos seguintes módulos para começarmos.\n'
    text += '\n'

    """text += '*GLPI*\n'
    text += '/criar\_chamado - Criar chamado\n'
    text += '/ver\_chamado - Acompanhar chamado\n'

    text += '\n'"""
    text += 'Caso não tenha uma opção para o que deseja, me diga do que precisa e vamos encontrar a solução juntos!'

    main_menu_keyboard = [
        [telegram.KeyboardButton('/GLPI')],
        [telegram.KeyboardButton('/SIGAA')],
    ]

    reply_kb_markup = telegram.ReplyKeyboardMarkup(main_menu_keyboard,
                                                   resize_keyboard=True,
                                                   one_time_keyboard=True)

    # Send the message with menu
    telegram_bot.send_message(
        parse_mode='Markdown',
        chat_id=chat['id'],
        text=text,
        reply_markup=reply_kb_markup)


def cancel_command(chat):
    pass


def unknown(chat):
    telegram_bot.send_message(chat_id=chat['id'], text='Desculpe, mas não me ensinaram a fazer isso ainda :/')


commands = {
    '/start': start,
    '/glpi': unknown,
    '/sigaa': unknown,
    '/cancelar': cancel_command,
}


# TODO: Create app for Messenger
class MessengerWebhookView(generic.View):
    def get(self, request, *args, **kwargs):
        if self.request.GET.get(u'hub.verify_token') == SECRET_KEY:
            return HttpResponse(self.request.GET['hub.challenge'])
        else:
            return HttpResponse('Error, invalid token')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return generic.View.dispatch(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        incoming_message = json.loads(self.request.body.decode('utf-8'))

        for entry in incoming_message['entry']:
            for message in entry['messaging']:
                if 'message' in message:
                    Bot.run_actions(wit_client, message)

        return HttpResponse()


# TODO: Create app for Telegram
class TelegramWebhookView(generic.View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return generic.View.dispatch(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        incoming_message = json.loads(request.body.decode('utf-8'))

        # TODO: Create message Model
        if incoming_message['message']:
            # message = incoming_message['message']
            chat_id = incoming_message['message']['chat']['id']
            message = incoming_message['message'].get('text')

            command = commands.get(message.split()[0].lower())  # check if command exist in list
            if command:
                command(incoming_message['message']['chat'])

                # pprint(json.loads(request.body.decode('utf-8')))

        return HttpResponse()


def get_curl_courses(request):
    pass
