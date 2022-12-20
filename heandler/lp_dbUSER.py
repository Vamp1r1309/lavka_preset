from config.config import ADMIN_ID
import sqlite3

class DataBase:

    def __init__(self, db_file):
        self.connect = sqlite3.connect(db_file)
        self.cursor = self.connect.cursor()

    async def add_users(self, user_id, user):
        with self.connect:
            return self.cursor.execute("""INSERT INTO users (user_id, user, role) VALUES (?, ?, ?)""",
                                       [user_id, user, 'admin' if user_id in ADMIN_ID else 'user'])

    async def add_presets(self, user_id, presets):
        with self.connect:
            return self.cursor.execute("""UPDATE users SET presets=(?) WHERE user_id=(?)""",
                                       [presets, user_id])

    async def check_presets(self, user_id):
        with self.connect:
            return self.cursor.execute("""SELECT presets FROM users WHERE user_id=(?)""",
                                       [user_id]).fetchone()
    
    
    async def update_null_users(self, user_id):
        return self.cursor.execute(("""UPDATE users SET bouth=(?), label=(?), presets=(?) WHERE user_id=(?)""",
                                       [False,1,'', user_id]))