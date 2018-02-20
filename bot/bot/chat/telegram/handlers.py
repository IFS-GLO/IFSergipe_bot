import telegram

from glpi.views import *

from bot.chat.models import *


def send_message(bot, chat, trigger):
    command = Command.objects.filter(trigger=trigger)[0]
    text = command.message

    if command.arguments is not None:
        # TODO: a function to check if exist more than one arg
        text = text.format(chat[command.arguments])

    bot.send_message(
        parse_mode='Markdown',
        chat_id=chat['id'],
        text=text,
    )

    if trigger == '/receber_notificacoes':
        chat = Chat.objects.get(id=int(chat['id']))
        chat.notification(True)

    elif trigger == '/cancelar_notificacoes':
        chat = Chat.objects.get(id=int(chat['id']))
        chat.notification(False)
