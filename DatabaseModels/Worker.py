import sqlite3

from main.config import database_path


class Worker:

    def __init__(self):
        self.connection = sqlite3.connect(database_path)
        self.connection.row_factory = sqlite3.Row

    def get_all_workers(self):
        cursor = self.connection.cursor()
        raw_data = cursor.execute('SELECT * FROM Worker')
        return [dict(row) for row in raw_data.fetchall()]

    def get_worker(self, user):
        query_data = (user.id,)
        cursor = self.connection.cursor()
        raw_data = cursor.execute('SELECT * FROM Worker INNER JOIN Post ON (Worker.Post_id = Post.Id)' +
                                           ' WHERE Telegram_id = ?', query_data)
        return dict(raw_data.fetchone())
