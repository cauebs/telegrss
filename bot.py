import logging
import config
from digrss import Digrss
from telegram import Bot
from telegram import InlineKeyboardButton as Button
from telegram import InlineKeyboardMarkup as Keyboard


logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(name)s - %(message)s')

bot = Bot(config.TOKEN)

with Digrss(interval=config.INTERVAL) as g:
    for entry in g:

        msg = "<b>{}</b>\n\n{}".format(entry.title, entry.summary)
        msg = msg.replace('<br>', '\n')

        keyboard = Keyboard([[Button(config.MORE, url=entry.link)]])
        bot.send_message(entry.target, text=msg, reply_markup=keyboard,
                         disable_web_page_preview=False, parse_mode="HTML")
