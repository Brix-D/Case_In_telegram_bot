from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from main.helpers.smiles import create_smile


def main_menu():
    keys = [
            [
                KeyboardButton(text="Покажи мне документацию" + create_smile("\\ud83d\\udcc4"))
            ],
            [
                KeyboardButton(text="Другие вопросы" + create_smile("\\u2753")),
                KeyboardButton(text="События" + create_smile("\\ud83d\\uddd3"))
            ]
        ]
    menu = ReplyKeyboardMarkup(keyboard=keys, resize_keyboard=True)
    return menu


def hide_menu():
    return ReplyKeyboardRemove()


def deadlines_menu():  # меню для просмотра и создания событий
    q_choice = [
        [
            KeyboardButton(text="Покажи мне события" + create_smile("\\ud83d\\uddd3")),
        ],
        [
            KeyboardButton(text="Создать событие" + create_smile("\\ud83d\\uddd3"))
        ],
        [
            KeyboardButton(text="В меню")
        ]
    ]
    menu = ReplyKeyboardMarkup(keyboard=q_choice, resize_keyboard=True)
    return menu


def question_menu():
    q_choice = [
        [
            KeyboardButton(text="Типичные вопросы" + create_smile("\\u2754"))
        ],
        [
            KeyboardButton(text="Задать вопрос" + create_smile("\\ud83d\\udcdd"))
        ],
        [
            KeyboardButton(text="Моя должность" + create_smile("\\ud83d\\udcbc"))
        ],
        [
            KeyboardButton(text="В меню")
        ]
    ]
    menu = ReplyKeyboardMarkup(keyboard=q_choice, resize_keyboard=True)
    return menu


def back_to_menu():
    q_choice = [
        [
            KeyboardButton(text="В меню")
        ]
    ]
    menu = ReplyKeyboardMarkup(keyboard=q_choice, resize_keyboard=True)
    return menu
