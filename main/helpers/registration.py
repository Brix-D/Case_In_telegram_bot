import sqlite3

from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from app import dispatcher, bot
from main.config import States, admin_id
from main.helpers.menu import back_to_menu, main_menu, hide_menu, check_new_users_menu
from DatabaseModels.Worker import Worker
from DatabaseModels.helpers.exceptions import PostNotFound, IdNotUnique


@dispatcher.message_handler(state=States.ENTER_EMAIL_STATE)
async def enter_email(message: Message, state: FSMContext):
    email = message.text
    async with state.proxy() as userdata:
        userdata["email"] = email
    global userdata_global
    async with state.proxy() as userdata:
        userdata_global = userdata
    # await message.answer(text="Введите вашу должность:", reply_markup=hide_menu())
    await message.answer(text="Ожидайте подверждения вашим работодателем", reply_markup=hide_menu())
    # await States.ENTER_POST_STATE.set()
    connection = Worker()
    try:
        connection.add_worker(message.from_user, userdata_global["email"])
    # except PostNotFound as post_err:
    #     text_message = "Такой должности не существует.\nПопробуйте ввести снова:"
    #     print(post_err)
    #     markup = hide_menu()
    except IdNotUnique as unique_err:
        print(unique_err)
    await bot.send_message(chat_id=admin_id, text="Поступили новые заявки на регистрацию:",
                           reply_markup=check_new_users_menu())

# @dispatcher.message_handler(state=States.ENTER_POST_STATE)
# async def enter_post(message: Message, state: FSMContext):
#     post = message.text
#     # global userdata_global
#     # async with state.proxy() as userdata:
#     #     userdata["post"] = post
#     # async with state.proxy() as userdata:
#     #     userdata_global = userdata
#
#     text_message = "Вы успешно зарегистрированы!"
