import sqlite3

from DatabaseModels.Worker import Worker
from DatabaseModels.helpers import exceptions
from main.config import database_path


class Admin(Worker):

    def __init__(self):
        super().__init__()

    def get_workers_without_post(self):
        cursor = self.connection.cursor()
        raw_data = cursor.execute("SELECT * FROM Worker WHERE Post_id is Null")
        result = raw_data.fetchall()
        dict_data = [dict(row) for row in result]
        return dict_data
