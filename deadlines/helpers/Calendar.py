import pickle

# from google_auth_oauthlib.flow import InstalledAppFlow
import httplib2
from aiogram.types import Message
from apiclient import discovery
from oauth2client.service_account import ServiceAccountCredentials
from oauth2client.client import HttpAccessTokenRefreshError

from main.config import client_secret_calendar, calendar_id, CALENDAR_TOKEN_PATH
from main.helpers.menu import back_to_menu


class Calendar:

    def __init__(self):
        scopes = ['https://www.googleapis.com/auth/calendar']
        credentials = pickle.load(open(CALENDAR_TOKEN_PATH, "rb"))
        self.connection = discovery.build("calendar", "v3", credentials=credentials)

    def get_events_for_range(self, date_start, date_end):
        events_result = self.connection.events().list(
            calendarId=calendar_id, timeMin=date_start, timeMax=date_end, maxResults=100, singleEvents=True,
            orderBy='startTime').execute()
        events = events_result.get('items', [])
        return events

    def create_event(self, eventdata):
        event = {
            'summary': eventdata["summary"],
            'description': eventdata["description"],
            'start': {
                'dateTime': eventdata["start_date"],
                'timeZone': 'Europe/Moscow',
            },
            'end': {
                'dateTime': eventdata["end_date"],
                'timeZone': 'Europe/Moscow',
            },
        }
        event = self.connection.events().insert(calendarId=calendar_id, body=event).execute()
        if event["status"] == 'confirmed':
            text_message = 'Событие успешно создано\n\n<a href="%s">Подробнее...</a>' % event['htmlLink']
            '<a href="%s">Подробнее...</a>'
        else:
            text_message = "Событие не создано"
        return [event["status"], text_message]

