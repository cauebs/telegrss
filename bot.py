import logging
import config
from digrss import Digrss
from telegram import Bot


logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s] %(name)s - %(message)s')

bot = Bot(config.TOKEN)

with Digrss(interval=config.INTERVAL) as g:
    for entry in g:

        msg = "<b>{}</b>\n\n{}".format(entry.title, entry.summary)
        msg += "\n<a href=\"{}\">{}</a>".format(entry.link, config.MORE)
        msg = msg.replace('<br>', '\n')

        bot.send_message(entry.target, text=msg, parse_mode="HTML",
                         disable_web_page_preview=True)
