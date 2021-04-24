from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, InlineKeyboardButton

from main.config import admin_id
from main.helpers.smiles import create_smile


def main_menu(user=None):
    """Главное меню"""
    keys = [
            [
                KeyboardButton(text="Покажи мне документацию" + create_smile("\\ud83d\\udcc4")),
                KeyboardButton(text="Сайт компании" + create_smile("\\ud83c\\udf10"))
            ],
            [
                KeyboardButton(text="Другие вопросы" + create_smile("\\u2753")),
                KeyboardButton(text="События" + create_smile("\\ud83d\\uddd3"))
            ]
        ]
    if user:
        if user.id == admin_id:
            keys.append(
                [
                    KeyboardButton(text="Просмотреть новые заявки")
                ]
            )
    menu = ReplyKeyboardMarkup(keyboard=keys, resize_keyboard=True)
    return menu


def hide_menu():
    """Скрыть меню"""
    return ReplyKeyboardRemove()


def deadlines_menu(user=None):
    """меню для просмотра и создания событий"""
    q_choice = [
        [
            KeyboardButton(text="Покажи мне события" + create_smile("\\ud83d\\uddd3")),
        ]
    ]
    if user.id == admin_id:
        q_choice.append([
            KeyboardButton(text="Создать событие" + create_smile("\\ud83d\\uddd3"))
        ])
    q_choice.append([
        KeyboardButton(text="В меню")
    ])

    menu = ReplyKeyboardMarkup(keyboard=q_choice, resize_keyboard=True)
    return menu


def question_menu():
    """Меню "другие вопросы" """
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
    """Меню назад"""
    q_choice = [
        [
            KeyboardButton(text="В меню")
        ]
    ]
    menu = ReplyKeyboardMarkup(keyboard=q_choice, resize_keyboard=True)
    return menu


def check_new_users_menu():
    """Меню панели админа"""
    q_choice = [
        [
            KeyboardButton(text="Просмотреть новые заявки")
        ]
    ]
    menu = ReplyKeyboardMarkup(keyboard=q_choice, resize_keyboard=True)
    return menu


def generate_workers_buttons(workers):
    """Меню для генерации кнопок с нвыми сотрудниками"""
    q_choice = []

    for worker in workers:
        print(worker)
        full_name = str(worker["Telegram_id"]) + " "
        full_name += worker["Firstname"] + " "
        if worker["Lastname"]:
            full_name += worker["Lastname"]

        q_choice.append([KeyboardButton(text=full_name)])
    q_choice.append([KeyboardButton(text="В меню")])
    menu = ReplyKeyboardMarkup(keyboard=q_choice, resize_keyboard=True)
    return menu
