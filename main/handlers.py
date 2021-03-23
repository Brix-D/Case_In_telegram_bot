from aiogram.dispatcher import FSMContext

from app import bot, dispatcher
from aiogram.types import Message
from aiogram.dispatcher.filters import Command, Text
import webbrowser

from main.config import admin_id, States, ROSATOM_SITE
from main.helpers.menu import main_menu, back_to_menu
from main.helpers.smiles import create_smile


async def on_start_message(dispatcher):
    """
    При запуске скрипта бота
    :param dispatcher:
    :return:
    """
    await bot.send_message(chat_id=admin_id, text="Бот запущен!",
                           reply_markup=main_menu())


async def on_finish_message(dispatcher):
    print("Бот остановлен!")


@dispatcher.message_handler(Command("start"), state="*")
async def start_conversation(message: Message):
    """
    При первом запуске бота
    :param message:
    :return:
    """
    # await message.answer(text="Бот запущен! Вот список возможных действий:\n" +
                             # "меню всегда можно вызвать с помощью команды /menu", reply_markup=main_menu())
    await States.ENTER_EMAIL_STATE.set()
    await message.answer(text="Давайте пройдем простую процедуру регистрации. Это займет не более двух минут")
    await message.answer(text="Введите ваш E-mail:", reply_markup=back_to_menu())


@dispatcher.message_handler(Command("menu"), state="*")
@dispatcher.message_handler(Text("В меню"), state="*")
async def general_menu(message: Message, state: FSMContext):
    """
    Команда показать меню
    :param state:
    :param message:
    :return:
    """
    # text = f"Получено сообщение: {message.text}"
    # # await bot.send_message(chat_id=message.from_user.id, text=text)
    # await message.answer(text=text)
    # state.proxy().clear()
    async with state.proxy() as userdata:
        userdata.clear()
    await message.answer(text="Выбери действие", reply_markup=main_menu())
    await States.COMMAND_STATE.set()


@dispatcher.message_handler(Text("Сайт компании" + create_smile("\\ud83c\\udf10")), state="*")
async def go_to_web_site(message: Message):
    webbrowser.open_new(ROSATOM_SITE)

    # TODO
