from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import asyncio
from main import config


# импорт хендлеров

# import documentation.handlers

# import deadlines.handlers
# import questions.handlers


loop = asyncio.get_event_loop()
bot = Bot(config.API_KEY, parse_mode="HTML")
dispatcher = Dispatcher(bot, loop=loop, storage=MemoryStorage())


def main():
    executor.start_polling(dispatcher, on_startup=on_start_message, on_shutdown=on_finish_message)


if __name__ == "__main__":
    from main.handlers import dispatcher, on_start_message, on_finish_message
    from documentation.handlers import show_documentation
    from deadlines.handlers import show_calendar_menu, create_event
    from questions.handlers import question_menu, other_questions, ask_new_question
    from main.helpers.registration import enter_email
    from admin.handlers import check_new_workers
    main()
