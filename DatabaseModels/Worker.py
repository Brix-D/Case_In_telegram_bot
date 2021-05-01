import mysql.connector as mysql

from main.config_dev import DB_HOSTNAME, DB_USERNAME, DB_PASSWORD, DB_DATABASE_NAME
from DatabaseModels.helpers import exceptions


class Worker:

    def __init__(self):
        self.connection = mysql.connect(
            host=DB_HOSTNAME,
            user=DB_USERNAME,
            passwd=DB_PASSWORD,
            database=DB_DATABASE_NAME,
        )

    def get_all_workers(self):
        cursor = self.connection.cursor(dictionary=True)
        raw_data = cursor.execute('SELECT * FROM worker')
        return [dict(row) for row in raw_data.fetchall()]

    def get_worker(self, user):
        query_data = (int(user.id),)
        cursor = self.connection.cursor(dictionary=True)
        stmt = "SELECT * FROM worker INNER JOIN post ON (worker.Post_id = post.Id) WHERE Telegram_id = %s"
        cursor.execute(stmt, query_data)
        data = cursor.fetchone()
        return data

    def add_worker(self, user, email):
        query_data = (user.id, user.first_name, user.last_name, email)
        cursor = self.connection.cursor(prepared=True,)
        sql_query = "INSERT INTO worker(Telegram_id, Firstname, Lastname, Email) VALUES (%s, %s, %s, %s)"
        try:
            cursor.execute(sql_query, query_data)
        except sqlite3.IntegrityError as IE:
            print(IE)
            if str(IE) == "UNIQUE constraint failed: Worker.Telegram_id":
                raise exceptions.IdNotUnique("Такой пользователь уже сщуествует")
            # elif str(IE) == "NOT NULL constraint failed: Worker.Post_id":
            #     raise exceptions.PostNotFound("Должность не найдена")
        self.connection.commit()

    @staticmethod
    def check_worker_exists(user):
        query_data = (user.id,)
        # connection = sqlite3.connect(database_path)
        connection = mysql.connect(
            host=DB_HOSTNAME,
            user=DB_USERNAME,
            passwd=DB_PASSWORD,
            database=DB_DATABASE_NAME,
        )
        cursor = connection.cursor(prepared=True,)
        cursor.execute("SELECT EXISTS (SELECT * FROM worker Where Telegram_id = %s AND Post_id is not NULL)", query_data)
        result_int = cursor.fetchone()[0]
        return bool(result_int)

    def close_connection(self):
        self.connection.close()
