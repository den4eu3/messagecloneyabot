from telegram.ext import Updater, MessageHandler, Filters
token = '6566025911:AAFmbbLc9_jcbG3rP0zXrPzZr4MFBbeLTZQ'


def echo(update, context):
    chat_id = update.message.chat_id
    message_text = update.message.text
    context.bot.send_message(chat_id=chat_id, text=message_text)


def main():
    updater = Updater(token, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text, echo))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()