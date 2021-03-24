from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from aiogram.dispatcher.filters import Text

from main.config import admin_id, States, Authorized_states
from app import bot, dispatcher
from main.handlers import general_menu
from main.helpers.menu import hide_menu, question_menu, back_to_menu
from main.helpers.smiles import create_smile
from DatabaseModels.Worker import Worker
import json
import codecs


@dispatcher.message_handler(Text("Другие вопросы" + create_smile("\\u2753")), state=Authorized_states)
async def other_questions(message: Message):
    """
    Меню "Другие вопросы" (название может меняться)
    :param message:
    :return:
    """
    await message.answer(text="Другие вопросы:\n", reply_markup=question_menu())


# Другие вопросы -> Типичные вопросы. Типичные вопросы можно прям тут описать - это нормальная практика.
# Штук 6-8 будет достаточно
@dispatcher.message_handler(Text("Типичные вопросы" + create_smile("\\u2754")), state=Authorized_states)
async def typical_questions(message: Message):
    """
    Команда типичные вопросы
    To Do: сделать считывание типичных вопросов из файла
    :param message:
    :return:
    """
    with codecs.open("questions\\typical_q.json", "r", "utf_8_sig") as file:
        json_str = file.read()
    list_question_obj = json.loads(json_str)
    for i in range(len(list_question_obj)):
         question = create_smile("\\u2705") + list_question_obj[i]['question'] + "\n\n" + list_question_obj[i]['answer']
         await message.answer(text=f"{question}")
    await message.answer(text="Если остались вопросы, вы можете задать их администатору.", reply_markup=back_to_menu())


# Другие вопросы -> Задать вопрос.
@dispatcher.message_handler(Text("Задать вопрос" + create_smile("\\ud83d\\udcdd")), state=Authorized_states)
async def ask_new_question(message: Message):
    """
    Команда задать новый вопрос
    :param message:
    :return:
    """
    await States.ENTER_QUESTION_STATE.set()
    await message.answer(text="Задать вопрос\n\nНапишите Ваш вопрос:\n\n\n",
                         reply_markup=back_to_menu())
# hmm


@dispatcher.message_handler(state=States.ENTER_QUESTION_STATE)
async def resend_message_to_boss(message: Message, state: FSMContext):
    """
    Перенаправляет сообщение начальнику (админу)
    :param message:
    :param state:
    :return:
    """
    await States.COMMAND_STATE.set()
    text = f"@{message.chat.username} задает вопрос: {message.text}"
    await bot.send_message(chat_id=admin_id, text=text)
    await message.answer(text="Ваш вопрос успешно задан.\nОтвет придёт вам в личные сообщения от администратора.\n")
    await general_menu(message, state)


@dispatcher.message_handler(Text("Моя должность" + create_smile("\\ud83d\\udcbc")), state=Authorized_states)
async def my_post(message: Message):
    """
    Выводит текущий статус сотрудника, его должность и ЗП
    :param message:
    :return:
    """
    connection = Worker()
    worker = connection.get_worker(message.from_user)
    text_html = f'<b>ФИО: </b><i>{worker["Firstname"]} {worker["Lastname"]}</i>\n' \
                f'<b>Должность: </b><i>{worker["Title"]}</i>\n' \
                f'<b>Зарплата: </b><i>{worker["Salary"]}</i>\n'
    await message.answer(text=text_html, parse_mode="HTML")
    # await message.answer(text=f'Должность: {worker["Title"]}', parse_mode="HTML")
    # await message.answer(text=f'Зарплата: {worker["Salary"]}', parse_mode="HTML")

