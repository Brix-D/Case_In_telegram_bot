from aiogram.types import Message
from aiogram.dispatcher.filters import Text

from app import dispatcher
from main.handlers import general_menu
from main.helpers.menu import back_to_menu, deadlines_menu
from main.helpers.smiles import create_smile

import httplib2
import datetime
import time
from main.config import client_secret_calendar, calendar_id
from apiclient import discovery
from oauth2client.service_account import ServiceAccountCredentials


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
    credentials = ServiceAccountCredentials.from_json_keyfile_name(client_secret_calendar,
                                                                   'https://www.googleapis.com/auth/calendar')
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)
    now = datetime.datetime.utcnow().isoformat() + 'Z'
    now_1week = round(time.time()) + 604800
    now_1week = datetime.datetime.fromtimestamp(now_1week).isoformat() + 'Z'
    events_result = service.events().list(
        calendarId=calendar_id, timeMin=now, timeMax=now_1week, maxResults=100, singleEvents=True,
        orderBy='startTime').execute()
    events = events_result.get('items', [])
    if not events:
        await message.answer(text='Нет событий на ближайшую неделю')
    else:
        msg = '<b>События на ближайшую неделю:</b>\n'
        for event in events:
            if not event['description']:
                ev_desc = 'Нет описания'
            else:
                ev_desc = event['description']
            ev_title = event['summary']
            cal_link = '<a href="%s">Подробнее...</a>' % event['htmlLink']
            ev_start = event['start'].get('dateTime')
            msg = msg + '%s\n%s\n%s\n%s\n\n' % (ev_title, ev_start, ev_desc, cal_link)
        await message.answer(msg, parse_mode='HTML')
        await general_menu(message)


@dispatcher.message_handler(Text("Создать событие" + create_smile("\\ud83d\\uddd3")), state="*")
async def create_event(message: Message):
    print('доделать')