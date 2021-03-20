from main import bot, dispatcher, executor

from aiogram.types import Message, ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.dispatcher.filters import Command, Text
from config import admin_id
from helpers.menu import generate_menu, hide_menu


async def on_start_message(dispatcher):
    await bot.send_message(chat_id=admin_id, text="Бот запущен! Вот список возможных действий:",
                           reply_markup=generate_menu())


@dispatcher.message_handler(Command("menu"))
async def show_menu(message: Message):
    # text = f"Получено сообщение: {message.text}"
    # # await bot.send_message(chat_id=message.from_user.id, text=text)
    # await message.answer(text=text)
    await message.answer(text="Выбери действие", reply_markup=generate_menu())


@dispatcher.message_handler(Text("Покажи мне документацию"))
async def show_documentation(message: Message):
    await message.answer(text="Вот список основных документов: \nВернутся в меню: /menu", reply_markup=hide_menu())


@dispatcher.message_handler(Text("Свяжи меня с начальником"))
async def connect_to_boss(message: Message):
    await message.answer(text="Вот форма связи: \nВернутся в меню: /menu", reply_markup=hide_menu())


@dispatcher.message_handler(Text("Покажи мне расписание"))
async def show_documentation(message: Message):
    await message.answer(text="Вот твой календарь: \nВернутся в меню: /menu", reply_markup=hide_menu())

