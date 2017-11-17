import telegram


def start(bot, chat):
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
    bot.send_message(
        parse_mode='Markdown',
        chat_id=chat['id'],
        text=text,
        reply_markup=reply_kb_markup)


def cancel_command(chat):
    pass


def unknown(bot, chat):
    bot.send_message(chat_id=chat['id'], text='Desculpe, mas não me ensinaram a fazer isso ainda :/')


commands = {
    '/start': start,
    '/glpi': unknown,
    '/sigaa': unknown,
    '/cancelar': cancel_command,
}
