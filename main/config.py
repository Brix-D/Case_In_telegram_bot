from aiogram.dispatcher.filters.state import StatesGroup, State
API_KEY = "1707075669:AAFn8IR85Ke-S9PFh2nwMnj2OiFQNN87iiI"
admin_id = 599361407
calendar_id = "s25kurvdk97a6qn1gvr92581o8@group.calendar.google.com"  # календарь в общем доступе
# client_secret_calendar = "deadlines\\client_secret.json"  # Google API Calendar
client_secret_calendar = "..\\deadlines\\client_secret.json"  # Google API Calendar
# путь для тех кто запускает через venv
documents_directory = "..\\documentation\\documentation_files"
database_path = "../Case_in_bot.db"


class States(StatesGroup):
    """
    Машина конечных состояний:
    у нас два сотстояния ввод текста и ввод команд
    также есть нулевое состояние, при запуске
    состояния переключатся при функциях вроде "задать вопрос"
    """
    COMMAND_STATE = State()
    ENTER_TEXT_STATE = State()
