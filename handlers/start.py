from aiogram import types
from aiogram import Dispatcher
from keyboards import main_menu

async def start_command(message: types.Message):
    user_name = message.from_user.first_name
    await message.answer(f"👋 Привет, {user_name}! Выберите действие:", reply_markup=main_menu)

def register_handlers_start(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=["start"])