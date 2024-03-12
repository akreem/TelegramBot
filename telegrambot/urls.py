from django.urls import path
from .views import main, send_telegram_message

urlpatterns = [
    path('', main),
    path('test', send_telegram_message)
]
