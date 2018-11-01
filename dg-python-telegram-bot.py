import os

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def handler(bot, update):
    update.effective_message.reply_text(update.effective_message.text + 'lol')


if __name__ == "__main__":
    # Set these variable to the appropriate values
    TOKEN = "494073850:AAFSGGw53qxhyyHwVLTJNyVfyjqTiaKoLBg"
    NAME = "fierce-woodland-12673"

    # Port is given by Heroku
    PORT = os.environ.get('PORT')

    # Set up the Updater
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    # Add handlers
    dp.add_handler(MessageHandler(Filters.text, handler))

    # Start the webhook
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook("https://{}.herokuapp.com/{}".format(NAME, TOKEN))
    updater.idle()
