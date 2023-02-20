from aiogram.types import ReplyKeyboardMarkup
from aiogram import types


def check_user_out_func():
    menu_default = ReplyKeyboardMarkup(resize_keyboard=True)
    menu_default.row("🎶 Музыка", "🎬 Кино", "📚 Книги")
    return menu_default

all_back_to_main_default = ReplyKeyboardMarkup(resize_keyboard=True)
all_back_to_main_default.row("⬅ На главную")
