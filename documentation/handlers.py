from aiogram.types import Message
from aiogram.dispatcher.filters import Text

import os

from app import dispatcher
from main.helpers.menu import hide_menu, back_to_menu
from documentation.helpers.send_document import upload_document, get_all_documents
from main.helpers.smiles import create_smile
from main.config_dev import documents_directory, Authorized_states


@dispatcher.message_handler(Text("Покажи мне документацию" + create_smile("\\ud83d\\udcc4")), state=Authorized_states)
async def show_documentation(message: Message):
    """
    Команда показать документацию
    :param message:
    :return:
    """
    await message.answer(text="Вот список основных документов: \n", reply_markup=back_to_menu())
    # directory = os.path.join("..", "documentation", "documentation_files")
    await message.answer(text="Список загружается, подождите немного")
    for file in get_all_documents(documents_directory):
        document = upload_document(os.path.join(documents_directory, file))
        await message.answer_document(document=document)