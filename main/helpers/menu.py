from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from main.helpers.smiles import create_smile


def main_menu():
    keys = [
            [
                KeyboardButton(text="Покажи мне документацию" + create_smile("\\ud83d\\udcc4"))
            ],
            [
                KeyboardButton(text="Другие вопросы" + create_smile("\\u2753")),
                KeyboardButton(text="Покажи мне расписание" + create_smile("\\ud83d\\uddd3"))
            ]
        ]
    menu = ReplyKeyboardMarkup(keyboard=keys, resize_keyboard=True)
    return menu


def hide_menu():
    return ReplyKeyboardRemove()


def question_menu():
    q_choice = [
        [
            KeyboardButton(text="Типичные вопросы" + create_smile("\\u2754"))
        ],
        [
            KeyboardButton(text="Задать вопрос" + create_smile("\\ud83d\\udcdd"))
        ]
    ]
    menu = ReplyKeyboardMarkup(keyboard=q_choice, resize_keyboard=True)
    return menu

