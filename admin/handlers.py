import sqlite3

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import Message, CallbackQuery

from DatabaseModels.admin import Admin
from DatabaseModels.helpers.exceptions import PostNotFound
from app import dispatcher, bot
from main.config import States, admin_id, Authorized_states
from main.helpers.menu import generate_workers_buttons, back_to_menu, main_menu


@dispatcher.message_handler(Text("Просмотреть новые заявки"), lambda message: message.from_user.id == admin_id,
                            state=Authorized_states)
async def check_new_workers(message: Message):
    admin = Admin()
    # print("обработчик сработал")
    waiting_workers = admin.get_workers_without_post()
    print(waiting_workers)
    if waiting_workers:
        await States.SELECT_WORKER_STATE.set()
        await message.answer(
            text="Новые заявки ожидают подтверждения. Выберите сотрудника и назначьте его на должность",
            reply_markup=generate_workers_buttons(waiting_workers))
    else:
        await message.answer(text="Новых заявок нет",
                             reply_markup=back_to_menu())


@dispatcher.message_handler(lambda message: message.from_user.id == admin_id, state=States.SELECT_WORKER_STATE)
# @dispatcher.callback_query_handler() #state=States.SELECT_WORKER_STATE)
async def select_new_worker(message: Message, state: FSMContext):  # callback_query: CallbackQuery
    # id_worker = callback_query.data
    # print(id_worker)
    # await bot.send_message(chat_id=admin_id, text=id_worker, reply_markup=back_to_menu())
    # admin = Admin()
    worker_id = message.text.split(' ')[0]
    async with state.proxy() as userdata:
        userdata["worker_id"] = worker_id
    await States.ENTER_POST_STATE.set()
    await message.answer(text="Выберите должность для данного сотрудника")


@dispatcher.message_handler(lambda message: message.from_user.id == admin_id, state=States.ENTER_POST_STATE)
async def select_post_for_worker(message: Message, state: FSMContext):
    global input_data
    async with state.proxy() as userdata:
        userdata["post"] = message.text
        input_data = userdata
    admin = Admin()
    try:
        admin.set_worker_post(input_data)
        await States.COMMAND_STATE.set()
    except PostNotFound as IE:
        print(IE)
        await message.answer(text="Ошибка присвоения должности: побробуйте еще")
    else:
        waiting_workers = admin.get_workers_without_post()
        print(waiting_workers)
        if waiting_workers:
            await States.SELECT_WORKER_STATE.set()
            await message.answer(
                text="Должность упешно назначена работнику. Есть другие завки",
                reply_markup=generate_workers_buttons(waiting_workers))
        else:
            await message.answer(text="Должность упешно назначена работнику. Новых заявок нет",
                                 reply_markup=back_to_menu())
        await bot.send_message(chat_id=input_data["worker_id"],
                               text="Администратор авторизовал вас. Для продолжения работы введите /start")

