import logging
import config
from digrss import Digrss
from telegram import Bot


logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(name)s - %(message)s')

bot = Bot(config.TOKEN)

with Digrss(interval=config.INTERVAL) as g:
    for entry in g:

        msg = f"<b>{entry.title}</b>\n\n{entry.summary}"
        msg += f"\n[{config.MORE}]({entry.link})"
        msg = msg.replace('<br>', '\n')

        bot.send_message(entry.target, text=msg, parse_mode="HTML",
                         disable_web_page_preview=False)
