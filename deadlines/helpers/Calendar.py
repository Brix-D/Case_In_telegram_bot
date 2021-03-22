import httplib2
from apiclient import discovery
from oauth2client.service_account import ServiceAccountCredentials

from main.config import client_secret_calendar, calendar_id


class Calendar:

    def __init__(self):
        credentials = ServiceAccountCredentials.from_json_keyfile_name(client_secret_calendar,
                                                                       'https://www.googleapis.com/auth/calendar')
        http = credentials.authorize(httplib2.Http())
        self.connection = discovery.build('calendar', 'v3', http=http)

    def get_events_for_range(self, date_start, date_end):
        events_result = self.connection.events().list(
            calendarId=calendar_id, timeMin=date_start, timeMax=date_end, maxResults=100, singleEvents=True,
            orderBy='startTime').execute()
        events = events_result.get('items', [])
        return events

    def create_event(self):
        # To Do
        pass
