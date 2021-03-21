from aiogram.types import Message
from aiogram.dispatcher.filters import Text

from app import dispatcher
from main.helpers.menu import hide_menu


@dispatcher.message_handler(Text("Покажи мне расписание"), state="*")
async def show_calendar(message: Message):
    """
    Команда показать каледарь
    :param message:
    :return:
    """
    await message.answer(text="Вот твой календарь: \nВернуться в меню: /menu", reply_markup=hide_menu())