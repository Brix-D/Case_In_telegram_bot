from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from aiogram.dispatcher.filters import Text

from oauth2client.client import HttpAccessTokenRefreshError

from app import dispatcher
from main.handlers import general_menu
from main.config import calendar_id, States, Authorized_states
from main.helpers.menu import back_to_menu, deadlines_menu, hide_menu, main_menu
from main.helpers.smiles import create_smile
from deadlines.helpers.Calendar import Calendar

from datetime import datetime
import time


@dispatcher.message_handler(Text("События" + create_smile("\\ud83d\\uddd3")), state=Authorized_states)
async def show_calendar(message: Message):
    """
    Меню "События" (название может меняться)
    :param message:
    :return:
    """
    await message.answer(text="Выбери действие: \n", reply_markup=deadlines_menu())


@dispatcher.message_handler(Text("Покажи мне события" + create_smile("\\ud83d\\uddd3")), state=Authorized_states)
async def show_calendar(message: Message):
    """
        Команда показывает события из общедоступного календаря
        :param message:
        :return:
        """
    try:
        calendar = Calendar()
        now = datetime.utcnow().isoformat() + 'Z'
        next_week = round(time.time()) + 604800
        next_week = datetime.fromtimestamp(next_week).isoformat() + 'Z'

        events_list = calendar.get_events_for_range(now, next_week)

        if not events_list:
            message_text = 'Нет событий на ближайшую неделю'
            await message.answer(text=message_text)
        else:
            message_text = '<b>События на ближайшую неделю:</b>\n'
            for event in events_list:
                if not event['description']:
                    event_description = 'Нет описания'
                else:
                    event_description = event['description']
                event_title = event['summary']
                full_calendar_link = '<a href="%s">Подробнее...</a>' % event['htmlLink']
                event_start = event['start'].get('dateTime')

                # message = message + '%s\n%s\n%s\n%s\n\n' % (event_title, event_start, event_description, full_calendar_link)

                message_text = message_text + f"\n{event_title}\n{event_start}\n{event_description}\n{full_calendar_link}\n"
    except HttpAccessTokenRefreshError as ex:
        message_text = "Токен доступа к календарю истек!"
        print(ex)
    await message.answer(text=message_text, parse_mode='HTML', reply_markup=back_to_menu())


@dispatcher.message_handler(Text("Создать событие" + create_smile("\\ud83d\\uddd3")), state=Authorized_states)
async def create_event(message: Message):
    await message.answer(text="Введите название события:", reply_markup=hide_menu())
    await States.ENTER_SUMMARY_STATE.set()


@dispatcher.message_handler(state=States.ENTER_SUMMARY_STATE)
async def enter_summary(message: Message, state: FSMContext):
    summary = message.text
    async with state.proxy() as userevent:
        userevent["summary"] = summary
    await message.answer(text="Введите место проведения события:", reply_markup=hide_menu())
    await States.ENTER_LOCATION_STATE.set()


@dispatcher.message_handler(state=States.ENTER_LOCATION_STATE)
async def enter_summary(message: Message, state: FSMContext):
    location = message.text
    async with state.proxy() as userevent:
        userevent["location"] = location
    await message.answer(text="Введите дату начала события в формате гггг-мм-дд:", reply_markup=hide_menu())
    await States.ENTER_DATESTART_STATE.set()


@dispatcher.message_handler(state=States.ENTER_DATESTART_STATE)
async def enter_date_start(message: Message, state: FSMContext):
    date_start = message.text
    global userevent_global
    async with state.proxy() as userevent:
        userevent["date_start"] = date_start
    async with state.proxy() as userevent:
        userevent_global = userevent
    await message.answer(text="Введите время начала события в формате чч:мм :", reply_markup=hide_menu())
    await States.ENTER_TIMESTART_STATE.set()


@dispatcher.message_handler(state=States.ENTER_TIMESTART_STATE)
async def enter_time_start(message: Message, state: FSMContext):
    time_start = message.text
    global userevent_global
    async with state.proxy() as userevent:
        userevent["time_start"] = time_start
    async with state.proxy() as userevent:
        userevent["start_date"] = str(userevent_global["date_start"] + 'T' + userevent_global["time_start"] + ':00+03:00')
    async with state.proxy() as userevent:
        userevent_global = userevent
    await message.answer(text="Введите дату окончания события в формате гггг-мм-дд:", reply_markup=hide_menu())
    await States.ENTER_DATEEND_STATE.set()


@dispatcher.message_handler(state=States.ENTER_DATEEND_STATE)
async def enter_date_end(message: Message, state: FSMContext):
    date_end = message.text
    async with state.proxy() as userevent:
        userevent["date_end"] = date_end
    async with state.proxy() as userevent:
        userevent_global = userevent
    await message.answer(text="Введите время окончания события в формате чч:мм :", reply_markup=hide_menu())
    await States.ENTER_TIMEEND_STATE.set()


@dispatcher.message_handler(state=States.ENTER_TIMEEND_STATE)
async def enter_time_end(message: Message, state: FSMContext):
    time_end = message.text
    global userevent_global
    async with state.proxy() as userevent:
        userevent["time_end"] = time_end
    async with state.proxy() as userevent:
        userevent["end_date"] = str(userevent_global["date_end"] + 'T' + userevent_global["time_end"] + ':00+03:00')
    async with state.proxy() as userevent:
        userevent_global = userevent
    await message.answer(text="Введите описание события:", reply_markup=hide_menu())
    await States.ENTER_DESCRIPTION_STATE.set()


@dispatcher.message_handler(state=States.ENTER_DESCRIPTION_STATE)
async def enter_description(message: Message, state: FSMContext):
    description = message.text
    async with state.proxy() as userevent:
        userevent["description"] = description
    async with state.proxy() as userevent:
        userevent_global = userevent
    calendar = Calendar()
    result = calendar.create_event(userevent_global)
    markup = main_menu()
    await message.answer(text=result[1], reply_markup=markup)
    await States.COMMAND_STATE.set()
