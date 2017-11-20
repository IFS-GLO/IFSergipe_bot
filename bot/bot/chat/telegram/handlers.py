import telegram

from glpi.views import *


def message_start(bot, chat):
    text = 'Opa ' + chat['first_name'] + '!\n'
    text += '\n'

    text += 'Sou um assistente virtual criado para te auxiliar. Escolha um dos seguintes módulos para começarmos.\n'
    text += '\n'

    text += '*GLPI*\n'
    text += '/criar\_chamado - Criar chamado\n'
    text += '/ver\_chamado - Visualiza informações\n'

    text += '\n'
    # text += 'Caso não tenha uma opção para o que deseja, me diga do que precisa e vamos encontrar a solução juntos!'

    """main_menu_keyboard = [
        [telegram.KeyboardButton('/GLPI')],
        [telegram.KeyboardButton('/SIGAA')],
    ]

    reply_kb_markup = telegram.ReplyKeyboardMarkup(
        main_menu_keyboard,
        resize_keyboard=True,
        one_time_keyboard=True
    )"""

    # Send the message with menu
    bot.send_message(
        parse_mode='Markdown',
        chat_id=chat['id'],
        text=text,
        # reply_markup=reply_kb_markup
    )


def message_cancel_command(chat):
    pass


def unknown(bot, chat):
    bot.send_message(chat_id=chat['id'], text='Desculpe, mas não me ensinaram a fazer isso ainda :/')


def message_glpi_help(bot, chat):
    text = 'Escolha uma das seguintes opções para prosseguir\n'
    text += '\n'
    text += '/novo\_chamado - Para cadastrar\n'
    text += '/ver\_chamado - Para visualizar\n'

    bot.send_message(chat_id=chat['id'], text=text)


def command_get_ticket_id(bot, chat):
    text = 'Informe o número do chamado'

    bot.send_message(chat_id=chat['id'], text=text)

    return {'next_command': get_ticket, 'template': message_ticket_info}  # next command


# TODO: Criar chamado
def message_title_ticket(bot, chat):
    text = 'Informe um título'

    bot.send_message(chat['id'], text=text)

    return {'next_command': message_content_ticket}


def message_content_ticket(bot, chat):
    text = 'Descreva o chamado'

    bot.send_message(chat['id'], text=text)

    return {'next_command': add_ticket}


def message_ticket_info(bot, chat, instance):
    end_sequence = True  # end of command sequence
    text = ''

    if instance['msg']:
        text = instance['text']

    else:
        instance = instance['instance']

        text += '*' + instance.name + '*\n'
        text += '\n'
        text += instance.content
        end_sequence = False

        main_menu_keyboard = [
            [telegram.KeyboardButton('/acompanhar_chamado')],
            [telegram.KeyboardButton('/ver_anexos')],
        ]

        reply_kb_markup = telegram.ReplyKeyboardMarkup(
            main_menu_keyboard,
            resize_keyboard=True,
            one_time_keyboard=True
        )

    bot.send_message(
        parse_mode='Markdown',
        chat_id=chat['id'],
        text=text,
        reply_markup=reply_kb_markup
    )

    return end_sequence


def message_get_documents(bot, chat, instance):
    pass


commands = {
    '/start': message_start,
    '/glpi': message_glpi_help,
    '/ver_chamado': command_get_ticket_id,
    '/criar_chamado': message_title_ticket,
    '/ver_anexos': message_get_documents,
    '/sigaa': unknown,
    '/cancelar': message_cancel_command,
}
