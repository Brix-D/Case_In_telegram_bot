from aiogram.dispatcher.filters.state import StatesGroup, State
API_KEY = "1787274187:AAFKOJPLmdbrIKVRRCi7LMAcL49Su042b74"
admin_id = 1011677109

# MySql database config
# ------------------------------
DB_HOSTNAME = "localhost"
DB_USERNAME = "root"
DB_PASSWORD = "Grossper123"
DB_DATABASE_NAME = "case_in_bot"
# ------------------------------

calendar_id = "shlyakhta4@gmail.com"  # календарь в общем доступе
client_secret_calendar = "deadlines\\client_secret.json"  # Google API Calendar
CALENDAR_TOKEN_PATH = "token.pkl"

documents_directory = "documentation\\documentation_files"
ROSATOM_SITE = "https://www.rosatom.ru/"


class States(StatesGroup):
    """
    Машина конечных состояний: есть сотстояния ввода текста и ввода команд
    также есть нулевое состояние, при запуске.
    состояния переключатся при функциях вроде "задать вопрос"
    """
    COMMAND_STATE = State()
    ENTER_QUESTION_STATE = State()
    ENTER_EMAIL_STATE = State()
    ENTER_POST_STATE = State()
    SELECT_WORKER_STATE = State()
    ENTER_SUMMARY_STATE = State()
    ENTER_DATESTART_STATE = State()
    ENTER_DATEEND_STATE = State()
    ENTER_TIMESTART_STATE = State()
    ENTER_TIMEEND_STATE = State()
    ENTER_DESCRIPTION_STATE = State()


Authorized_states = [
    None,
    States.COMMAND_STATE,
    States.ENTER_QUESTION_STATE,
    States.SELECT_WORKER_STATE,
    States.ENTER_SUMMARY_STATE,
    States.ENTER_DATESTART_STATE,
    States.ENTER_DATEEND_STATE,
    States.ENTER_TIMESTART_STATE,
    States.ENTER_TIMEEND_STATE,
    States.ENTER_DESCRIPTION_STATE,
]
