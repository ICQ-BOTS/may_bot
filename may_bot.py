from bot.bot import Bot
from bot.handler import MessageHandler, BotButtonCommandHandler, DefaultHandler
from server import button_processing, message_processing
import config


bot = Bot(token=config.TOKEN)
bot.dispatcher.add_handler(MessageHandler(callback=message_processing))
bot.dispatcher.add_handler(BotButtonCommandHandler(callback=button_processing))
bot.start_polling()
bot.idle()