from aiogram.types import Message
from aiogram.dispatcher.filters import Text

import os

from app import dispatcher
from main.helpers.menu import hide_menu, back_to_menu
from documentation.helpers.send_document import upload_document, get_all_documents
from main.helpers.smiles import create_smile


@dispatcher.message_handler(Text("Покажи мне документацию" + create_smile("\\ud83d\\udcc4")), state="*")
async def show_documentation(message: Message):
    """
    Команда показать документацию
    :param message:
    :return:
    """
    await message.answer(text="Вот список основных документов: \n", reply_markup=back_to_menu())
    directory = os.path.join("..", "documentation", "documentation_files")
    for file in get_all_documents(directory):
        document = upload_document(os.path.join(directory, file))
        await message.answer_document(document=document, caption="Техника безопасности на АЭС")