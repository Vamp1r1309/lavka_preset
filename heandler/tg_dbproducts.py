from config.config import ADMIN_ID
import sqlite3

class DataBaseProducts:

    def __init__(self, db_file):
        self.connect = sqlite3.connect(db_file)
        self.cursor = self.connect.cursor()

    async def id_products(self, presets):
        with self.connect:
            return self.cursor.execute("""SELECT file_products FROM goods WHERE products=(?)""",[presets]).fetchone()[0]