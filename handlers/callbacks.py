from aiogram import types
from aiogram import Dispatcher

from bot import dp
from joke_api import get_joke


async def start_command(message: types.Message):
    user_name = message.from_user.first_name

@dp.callback_query_handler(lambda call: True)
async def handle_callback(call: types.CallbackQuery):
    if call.data == "image":
        await call.message.answer("📷 Выберите категорию картинки (футбол, бокс, баскетбол)")
    elif call.data == "weather":
        await call.message.answer("🌦 Введите название города, чтобы узнать погоду")
    elif call.data == "currency":
        await call.message.answer("💰 Текущий курс валют: ...")
    elif call.data == "movies":
        await call.message.answer("🎬 Вот список фильмов: ...")
    elif call.data == "joke":
        joke = await get_joke(category="Programming", blacklist="nsfw,religious")
        await call.message.answer(joke)
    else:
        await call.message.answer("❌ Неизвестная команда")