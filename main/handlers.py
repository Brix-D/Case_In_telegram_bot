import distutils

from main import bot, dispatcher
import os
from aiogram.types import Message
from aiogram.dispatcher.filters import Command, Text
from config import admin_id
from helpers.menu import generate_menu, hide_menu, question_menu
from helpers.send_document import upload_document, get_all_documents


async def on_start_message(dispatcher):
    await bot.send_message(chat_id=admin_id, text="Бот запущен!",
                           reply_markup=generate_menu())


@dispatcher.message_handler(Command("start"))
async def start_conversation(message: Message):
    await message.answer(text="Бот запущен! Вот список возможных действий:\n" +
                              "меню всегда можно вызвать с помощью команды /menu", reply_markup=generate_menu())


@dispatcher.message_handler(Command("menu"))
async def show_menu(message: Message):
    # text = f"Получено сообщение: {message.text}"
    # # await bot.send_message(chat_id=message.from_user.id, text=text)
    # await message.answer(text=text)
    await message.answer(text="Выбери действие", reply_markup=generate_menu())


@dispatcher.message_handler(Text("Покажи мне документацию"))
async def show_documentation(message: Message):
    await message.answer(text="Вот список основных документов: \nВернуться в меню: /menu", reply_markup=hide_menu())
    directory = "documentation_files"
    for file in get_all_documents(directory):
        document = upload_document(os.path.join(directory, file))
        await message.answer_document(document=document, caption="Техника безопасности на АЭС")


@dispatcher.message_handler(Text("Покажи мне расписание"))
async def show_documentation(message: Message):
    await message.answer(text="Вот твой календарь: \nВернуться в меню: /menu", reply_markup=hide_menu())

# Меню "Другие вопросы" (название может меняться)
@dispatcher.message_handler(Text("Другие вопросы"))
async def connect_to_boss(message: Message):
    await message.answer(text="Другие вопросы: \nВернуться в меню: /menu", reply_markup=question_menu())
    # Другие вопросы -> Типичные вопросы. Типичные вопросы можно прям тут описать - это нормальная практика. Штук 6-8 будет достаточно
    @dispatcher.message_handler(Text("Типичные вопросы"))
    async def connect_to_typical_q(message: Message):
        await message.answer(text="Типичные вопросы: \nГде находится Мадагаскар? - На острове Мадагаскар!\nВернуться в меню: /menu", reply_markup=question_menu())
    # Другие вопросы -> Задать вопрос.
    @dispatcher.message_handler(Text("Задать вопрос"))
    async def connect_to_new_q(message: Message):
        global NEW_QUESTION_FLAG
        NEW_QUESTION_FLAG = 'True'
        await message.answer(text="Задать вопрос\n\nНапишите Ваш вопрос:\n\n\nДля отмены - вернуться в меню: /menu", reply_markup=hide_menu())
    # hmm
    @dispatcher.message_handler()
    async def echo(message: Message):
        global NEW_QUESTION_FLAG
        NEW_QUESTION_FLAG = NEW_QUESTION_FLAG.lower()
        bool_n_q = bool(NEW_QUESTION_FLAG)
        if(bool_n_q == True):
            text = f"@{message.chat.username} задает вопрос: {message.text}"
            NEW_QUESTION_FLAG = ''
            await bot.send_message(chat_id=admin_id, text=text)
            await message.answer(text="Ваш вопрос успешно задан.\n Ответ придёт вам в личные сообщения от администратора.\n Вернуться в меню: /menu")