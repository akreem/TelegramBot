from django.shortcuts import render
from django.http import HttpResponse
from .telegram_api import TelegramAPI
# Create your views here.

def main(request):
    return HttpResponse('ok')

def send_telegram_message(request):
    # Replace 'your_bot_token' with the actual token obtained from the BotFather
    bot_token = '6356306608:AAEa1QFKCXjmBtuJj4P2JhePv7qB0pMddOQ'
    telegram_api = TelegramAPI(bot_token)

    # Replace 'your_chat_id' with the actual chat ID where you want to send the message
    chat_id = '5890316032'
    message_text = 'Hello from your Django app!'
    
    # Send a simple text message
    telegram_api.send_message(chat_id, message_text)

    return HttpResponse("Message sent to Telegram!")