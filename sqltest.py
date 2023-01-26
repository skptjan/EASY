import sqlite3
from sqlite3 import Error
from enum import StrEnum
import datetime
import pytz
tz = pytz.timezone('europe/Amsterdam')

class Tables(StrEnum):
    Profile = "Frontend_profile"
    LampLog = "Frontend_lamplog"

class TablesColumn(StrEnum):
    Profile = "Frontend_profile"
    LampLog = "([user_id], [time], [on])"

def LampLogMapper(user, on):
        return "(%s, '%s', %s)" % (user, datetime.datetime.now(tz), on)

db = "C:\\Users\\stjan\\PycharmProjects\\EASY\\EASY\\db.sqlite3"

def execute(db_file, query):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        c = conn.cursor()
        # print(query)
        res = c.execute(query)
        conn.commit()
        
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def get(db_file, query):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        c = conn.cursor()
        # print(query)
        res = c.execute(query)
        return res.fetchone()
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
