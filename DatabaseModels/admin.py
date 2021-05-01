from DatabaseModels.Worker import Worker
from DatabaseModels.helpers import exceptions


class Admin(Worker):

    def __init__(self):
        super().__init__()

    def get_workers_without_post(self):
        cursor = self.connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM worker WHERE Post_id is Null")
        result = cursor.fetchall()
        # dict_data = [dict(row) for row in result]
        return result

    def set_worker_post(self, userdata):
        cursor = self.connection.cursor(prepared=True,)
        post_data = (userdata["post"],)
        cursor.execute('SELECT Id FROM post WHERE Title = %s ', post_data)
        select_post_id = cursor.fetchone()
        print(select_post_id)
        if not select_post_id:
            raise exceptions.PostNotFound('Должность не найдена')
        else:

            query_data = (select_post_id[0], userdata["worker_id"],)

            cursor.execute("UPDATE worker SET Post_id = %s WHERE Telegram_id = %s", query_data)
            self.connection.commit()
