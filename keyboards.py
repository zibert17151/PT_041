from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


joke_category_keyboard = InlineKeyboardMarkup(row_width=2)
joke_category_keyboard.add(
    InlineKeyboardButton(text="Программисты", callback_data="joke_Programming"),
    InlineKeyboardButton(text="Черный юмор", callback_data="joke_Dark"),
    InlineKeyboardButton(text="Общая", callback_data="joke_Any"),
    InlineKeyboardButton(text="Без политики", callback_data="joke_nopolitics")
)
keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="📸 Картинка", callback_data="image"),
        InlineKeyboardButton(text="⛅ Погода", callback_data="weather")
    ],
    [
        InlineKeyboardButton(text="💰 Курс валют", callback_data="currency"),
        InlineKeyboardButton(text="🎬 Список фильмов", callback_data="movies")
    ],
    [
        InlineKeyboardButton(text="🤣 Шутка", callback_data="joke"),
        InlineKeyboardButton(text="📋 Опрос", callback_data="survey")
    ]
])


def main_menu():
    return None