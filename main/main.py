from aiogram import Bot, Dispatcher, executor
import asyncio
import config

loop = asyncio.get_event_loop()
bot = Bot(config.API_KEY, parse_mode="HTML")
dispatcher = Dispatcher(bot, loop=loop)

if __name__ == "__main__":
    from handlers import dispatcher, on_start_message
    executor.start_polling(dispatcher, on_startup=on_start_message)
