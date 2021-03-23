import sqlite3

from main.config import database_path
from DatabaseModels.helpers import exceptions

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

    def add_worker(self, user, email, post):
        query_data = (user.id, user.first_name, user.last_name, email, post)
        cursor = self.connection.cursor()
        sql_query = "INSERT INTO Worker(Telegram_id, Firstname, Lastname, Email, Post_id) VALUES (?, ?, ?, ?, (SELECT Id FROM Post WHERE Title = ?))"
        try:
            cursor.execute(sql_query, query_data)
        except sqlite3.IntegrityError as IE:
            print(IE)
            if str(IE) == "UNIQUE constraint failed: Worker.Telegram_id":
                raise exceptions.IdNotUnique("Такой пользователь уже сщуествует")
            elif str(IE) == "NOT NULL constraint failed: Worker.Post_id":
                raise exceptions.PostNotFound("Должность не найдена")
        self.connection.commit()
