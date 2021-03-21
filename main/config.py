from aiogram.dispatcher.filters.state import StatesGroup, State
API_KEY = "1707362497:AAFSyW_HreeIUZ-5DSdk5xFDe_DCWyIUB8M"

admin_id = 1011677109


class States(StatesGroup):
    """
    Машина конечных состояний:
    у нас два сотстояния ввод текста и ввод команд
    также есть нулевое состояние, при запуске
    состояния переключатся при функциях вроде "задать вопрос"
    """
    COMMAND_STATE = State()
    ENTER_TEXT_STATE = State()
