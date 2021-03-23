from aiogram.dispatcher.filters.state import StatesGroup, State
API_KEY = "1707362497:AAFSyW_HreeIUZ-5DSdk5xFDe_DCWyIUB8M"
admin_id = 1011677109
calendar_id = "s25kurvdk97a6qn1gvr92581o8@group.calendar.google.com"  # календарь в общем доступе
# client_secret_calendar = "deadlines\\client_secret.json"  # Google API Calendar
client_secret_calendar = "..\\deadlines\\client_secret.json"  # Google API Calendar
# путь для тех кто запускает через venv
CALENDAR_TOKEN_PATH = "..\\token.pkl"
documents_directory = "..\\documentation\\documentation_files"
database_path = "../Case_in_bot.db"
ROSATOM_SITE = "https://www.rosatom.ru/"


class States(StatesGroup):
    """
    Машина конечных состояний:
    у нас два сотстояния ввод текста и ввод команд
    также есть нулевое состояние, при запуске
    состояния переключатся при функциях вроде "задать вопрос"
    """
    COMMAND_STATE = State()
    ENTER_QUESTION_STATE = State()
    ENTER_EMAIL_STATE = State()
    ENTER_POST_STATE = State()
