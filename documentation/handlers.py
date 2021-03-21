from aiogram.types import Message
from aiogram.dispatcher.filters import Text

import os

from app import dispatcher
from main.helpers.menu import hide_menu
from documentation.helpers.send_document import upload_document, get_all_documents


@dispatcher.message_handler(Text("Покажи мне документацию"), state="*")
async def show_documentation(message: Message):
    """
    Команда показать документацию
    :param message:
    :return:
    """
    await message.answer(text="Вот список основных документов: \nВернуться в меню: /menu", reply_markup=hide_menu())
    directory = os.path.join("..", "documentation", "documentation_files")
    for file in get_all_documents(directory):
        document = upload_document(os.path.join(directory, file))
        await message.answer_document(document=document, caption="Техника безопасности на АЭС")