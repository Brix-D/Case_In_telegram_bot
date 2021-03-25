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

    def set_worker_post(self, userdata):
        cursor = self.connection.cursor()
        post_data = (userdata["post"],)
        select_post_raw = cursor.execute('SELECT Id FROM Post WHERE Title = ? ', post_data)
        select_post_id = select_post_raw.fetchone()
        print(select_post_id)
        if not select_post_id:
            raise exceptions.PostNotFound('Должность не найдена')
        else:

            query_data = (select_post_id[0], userdata["worker_id"],)

            cursor.execute("UPDATE Worker SET Post_id = ? WHERE Telegram_id = ?", query_data)
            self.connection.commit()
