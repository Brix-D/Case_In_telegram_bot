from aiogram.dispatcher.filters import Text
from aiogram.types import Message

from DatabaseModels.admin import Admin
from app import dispatcher
from main.config import States, admin_id, Authorized_states
from main.helpers.menu import generate_workers_buttons, back_to_menu


@dispatcher.message_handler(Text("Просмотреть новые заявки"), lambda message: message.from_user.id == admin_id,
                            state=Authorized_states)
async def check_new_workers(message: Message):
    admin = Admin()
    # print("обработчик сработал")
    waiting_workers = admin.get_workers_without_post()
    print(waiting_workers)
    if waiting_workers:
        await States.SELECT_WORKER_STATE.set()
        await message.answer(text="Новые заявки ожидают потдерждения. Выберите сотрудника и назначьте его на должность",
                             reply_markup=generate_workers_buttons(waiting_workers))
    else:
        await message.answer(text="Новых заявок нет",
                             reply_markup=back_to_menu())
