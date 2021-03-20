from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton


def generate_menu():
    keys = [
            [
                KeyboardButton(text="Покажи мне документацию")
            ],
            [
                KeyboardButton(text="Свяжи меня с начальником"),
                KeyboardButton(text="Покажи мне расписание")
            ]
        ]
    menu = ReplyKeyboardMarkup(keyboard=keys, resize_keyboard=True)
    return menu


def hide_menu():
    return ReplyKeyboardRemove()