# telegram_api.py
from telegram import Bot
from telegram.constants import ParseMode

class TelegramAPI:
    def __init__(self, bot_token):
        self.bot = Bot(token=bot_token)

    def send_message(self, chat_id, text, parse_mode=ParseMode.MARKDOWN):
        self.bot.send_message(chat_id=chat_id, text=text, parse_mode=parse_mode)
