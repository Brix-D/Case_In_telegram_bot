from aiogram.types import Message
from aiogram.dispatcher.filters import Text

from apiclient import discovery
from oauth2client.client import HttpAccessTokenRefreshError
from oauth2client.service_account import ServiceAccountCredentials

from app import dispatcher
from main.handlers import general_menu
from main.config import client_secret_calendar, calendar_id
from main.helpers.menu import back_to_menu, deadlines_menu
from main.helpers.smiles import create_smile
from deadlines.helpers.Calendar import Calendar

import httplib2
import datetime
import time


@dispatcher.message_handler(Text("События" + create_smile("\\ud83d\\uddd3")), state="*")
async def show_calendar(message: Message):
    """
    Меню "События" (название может меняться)
    :param message:
    :return:
    """
    await message.answer(text="Выбери действие: \n", reply_markup=deadlines_menu())


@dispatcher.message_handler(Text("Покажи мне события" + create_smile("\\ud83d\\uddd3")), state="*")
async def show_calendar(message: Message):
    """
        Команда показывает события из общедоступного календаря
        :param message:
        :return:
        """
    try:
        calendar = Calendar()
        now = datetime.datetime.utcnow().isoformat() + 'Z'
        next_week = round(time.time()) + 604800
        next_week = datetime.datetime.fromtimestamp(next_week).isoformat() + 'Z'

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

                message_text = message_text + f"{event_title}\n{event_start}\n{event_description}\n\n\n{full_calendar_link}"
    except HttpAccessTokenRefreshError as ex:
        message_text = "Токен доступа к календарю истек!"
        print(ex)
    await message.answer(text=message_text, parse_mode='HTML', reply_markup=back_to_menu())


@dispatcher.message_handler(Text("Создать событие" + create_smile("\\ud83d\\uddd3")), state="*")
async def create_event(message: Message):
    print('доделать')