from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton


def main_menu():
    keys = [
            [
                KeyboardButton(text="Покажи мне документацию")
            ],
            [
                KeyboardButton(text="Другие вопросы"),
                KeyboardButton(text="Покажи мне расписание")
            ]
        ]
    menu = ReplyKeyboardMarkup(keyboard=keys, resize_keyboard=True)
    return menu


def hide_menu():
    return ReplyKeyboardRemove()


def question_menu():
    q_choice = [
        [
            KeyboardButton(text="Типичные вопросы")
        ],
        [
            KeyboardButton(text="Задать вопрос")
        ]
    ]
    menu = ReplyKeyboardMarkup(keyboard=q_choice, resize_keyboard=True)
    return menu

