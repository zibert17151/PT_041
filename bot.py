import os
import types
from email import message

import requests
from aiogram import Bot, Dispatcher, F, Router
from aiogram.dispatcher.middlewares import data
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.utils.keyboard import ReplyKeyboardMarkup, KeyboardButton
from dotenv import load_dotenv
from pyexpat.errors import messages

load_dotenv()

TOKEN = os.getenv('TELEGRAM_API_TOKEN')
TOKEN1 = os.getenv('WEATHER_API_KEY')
bot = Bot(token=TOKEN)
dp = Dispatcher()
router = Router()

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📸 Картинка", callback_data="image"),
         KeyboardButton(text="⛅ Погода", callback_data="weather")
        ],
        #
        [KeyboardButton(text="💰 Курс валют", callback_data="currency"), KeyboardButton(text="🎬 Список фильмов", callback_data="movies")],
        [KeyboardButton(text="🤣 Joke", callback_data="joke")]
    ],
    resize_keyboard=True
)


@router.message(Command("start"))
async def start_command(message: Message):
    user_name = message.from_user.first_name
    await message.answer(
        f"👋 Привет, {user_name}! Выберите действие:", reply_markup=main_menu
    )




async def main():
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())



@bot.message_handler(content_types=["text"])
def get_weather(message):
    markup = types.InlineKeyboardMarkup()
    btn_1 = KeyboardButton(text="🌦 Погода", callback_data="weather")
    # city = message.text.strip().lower()
    # res = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={TOKEN1}&units=metric&lang=ru")
    # bot.reply_to(message, f"Сейчас погода: {res.json()}")

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'weather':
        city = message.text.strip().lower()
        res = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={TOKEN1}&units=metric&lang=ru")
        bot.reply_to(message, f"Сейчас погода: {res.json()}")


