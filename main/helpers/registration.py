import sqlite3

from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from app import dispatcher
from main.config import States
from main.helpers.menu import back_to_menu, main_menu, hide_menu
from DatabaseModels.Worker import Worker
from DatabaseModels.helpers.exceptions import PostNotFound, IdNotUnique


@dispatcher.message_handler(state=States.ENTER_EMAIL_STATE)
async def enter_email(message: Message, state: FSMContext):
    email = message.text
    async with state.proxy() as userdata:
        userdata["email"] = email
    await message.answer(text="Введите вашу должность:", reply_markup=hide_menu())
    await States.ENTER_POST_STATE.set()


@dispatcher.message_handler(state=States.ENTER_POST_STATE)
async def enter_post(message: Message, state: FSMContext):
    post = message.text
    global userdata_global
    async with state.proxy() as userdata:
        userdata["post"] = post
    async with state.proxy() as userdata:
        userdata_global = userdata
    connection = Worker()
    text_message = "Вы успешно зарегистрированны!"
    try:
        connection.add_worker(message.from_user, userdata_global["email"], userdata_global["post"])
    except PostNotFound as post_err:
        text_message = "Такой должности не существует.\nПопробуйте ввести снова:"
        print(post_err)
        markup = hide_menu()
    except IdNotUnique as unique_err:
        text_message = "Вы уже зарегистрированы"
        print(unique_err)
        markup = main_menu()
        await States.COMMAND_STATE.set()
    else:
        await States.COMMAND_STATE.set()
        markup = main_menu()
    await message.answer(text=text_message, reply_markup=markup)

