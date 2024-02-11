from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

user_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, keyboard=[
    [
        KeyboardButton(text="Відкрити меню"),
        KeyboardButton(text="Допомога")
    ]
])

menu_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, keyboard=[
    [KeyboardButton(text="Зробити документ")],
    [KeyboardButton(text="Допомога")]
])
