import sqlite3

class DBController():
    dbname = ""
    db = ""

    def __init__(self, dbname):
        self.dbname = dbname
        self.connect()

    def connect(self):
        self.db = sqlite3.connect(self.dbname)

    def getAllCards(self):
        return self.db.execute("SELECT * FROM cards").fetchall()
