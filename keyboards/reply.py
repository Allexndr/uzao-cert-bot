from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🔄 Начать новый сертификат")]
    ],
    resize_keyboard=True,
    one_time_keyboard=False
)