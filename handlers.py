import os
import json
import requests
from aiogram import Bot, Dispatcher, F, Router
from aiogram.types import message
from aiogram.filters import Command
from aiogram.utils.keyboard import ReplyKeyboardMarkup, KeyboardButton
from dotenv import load_dotenv
TOKEN = os.getenv('TELEGRAM_API_TOKEN')
TOKEN1 = os.getenv('WEATHER_API_KEY')
bot = Bot(token=TOKEN)


#
@bot.message_handler(content_types=["text"])
def get_weather(message):    city = message.text.strip().lower()
res = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={TOKEN1}&units=metric&lang=ru")
data = json.loads(res.text)
bot.reply_to(message, f"Сейчас погода: {data['main']['temp']}")
