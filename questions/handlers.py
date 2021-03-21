from aiogram.types import Message
from aiogram.dispatcher.filters import Text

from main.config import admin_id, States
from app import bot, dispatcher
from main.handlers import general_menu
from main.helpers.menu import hide_menu, question_menu


@dispatcher.message_handler(Text("Другие вопросы"), state="*")
async def other_questions(message: Message):
    """
    Меню "Другие вопросы" (название может меняться)
    :param message:
    :return:
    """
    await message.answer(text="Другие вопросы: \nВернуться в меню: /menu", reply_markup=question_menu())


# Другие вопросы -> Типичные вопросы. Типичные вопросы можно прям тут описать - это нормальная практика.
# Штук 6-8 будет достаточно
@dispatcher.message_handler(Text("Типичные вопросы"), state="*")
async def typical_questions(message: Message):
    """
    Команда типичные вопросы
    To Do: сделать считывание типичных вопросов из файла
    :param message:
    :return:
    """
    await message.answer(text="Типичные вопросы: \nГде находится Мадагаскар? - На острове Мадагаскар!" +
                              "\nВернуться в меню: /menu",
                         reply_markup=question_menu())


# Другие вопросы -> Задать вопрос.
@dispatcher.message_handler(Text("Задать вопрос"), state="*")
async def ask_new_question(message: Message):
    """
    Команда задать новый вопрос
    :param message:
    :return:
    """
    await States.ENTER_TEXT_STATE.set()
    await message.answer(text="Задать вопрос\n\nНапишите Ваш вопрос:\n\n\nДля отмены - вернуться в меню: /menu", reply_markup=hide_menu())
# hmm


@dispatcher.message_handler(state=States.ENTER_TEXT_STATE)
async def resend_message_to_boss(message: Message):
    """
    Перенаправляет сообщение начальнику (админу)
    :param message:
    :return:
    """
    await States.COMMAND_STATE.set()
    text = f"@{message.chat.username} задает вопрос: {message.text}"
    await bot.send_message(chat_id=admin_id, text=text)
    await message.answer(text="Ваш вопрос успешно задан.\nОтвет придёт вам в личные сообщения от администратора.\nВернуться в меню: /menu")
    await general_menu(message)
