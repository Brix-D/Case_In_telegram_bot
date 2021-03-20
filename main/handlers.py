from main import bot, dispatcher, executor

from aiogram.types import Message
from config import admin_id


async def send_to_admin(dispatcher):
    await bot.send_message(chat_id=admin_id, text="Бот запущен!")


@dispatcher.message_handler()
async def receive_last_message(message: Message):
    text = f"Получено сообщение: {message.text}"
    # await bot.send_message(chat_id=message.from_user.id, text=text)
    await message.answer(text=text)

