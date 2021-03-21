from aiogram.types import Message
from aiogram.dispatcher.filters import Text

from app import dispatcher
from main.helpers.menu import hide_menu, back_to_menu
from main.helpers.smiles import create_smile


@dispatcher.message_handler(Text("Покажи мне расписание" + create_smile("\\ud83d\\uddd3")), state="*")
async def show_calendar(message: Message):
    """
    Команда показать каледарь
    :param message:
    :return:
    """
    await message.answer(text="Вот твой календарь: \n", reply_markup=back_to_menu())
