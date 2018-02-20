def send_message(bot, chat, text, *args):
    bot.send_message(
        parse_mode='Markdown',
        chat_id=chat['id'],
        text=text,
    )
