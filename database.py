import sqlite3
from typing import Union
import datetime
import json

def get_userx(user_id):
    with sqlite3.connect(path_to_db) as db:
        users = db.execute(f"SELECT balance FROM 'storage_users' WHERE user_id=?", [user_id]).fetchall()
        return users

def get_user_balance_and_id(user_id):
    with sqlite3.connect(path_to_db) as db:
        users = db.execute(f"SELECT * FROM 'storage_users' WHERE user_id=?", [user_id]).fetchall()
        return users

def check_for_wait():
    with sqlite3.connect(path_to_db) as db:
            id = db.execute("SELECT * FROM waiting").fetchall()
            db.commit()
            return id

def delete_wait(user_id):
    with sqlite3.connect(path_to_db) as db:
        db.execute(f"DELETE FROM 'waiting' WHERE user_id=?", [user_id])
        db.commit()

def get_money(user_id):
    with sqlite3.connect(path_to_db) as db:
        users = db.execute(f"SELECT balance FROM 'storage_users' WHERE user_id=?", [user_id]).fetchall()
        print(users)
        return users

def get_wait(user_id):
    with sqlite3.connect(path_to_db) as db:
            id = db.execute(f"SELECT rowid FROM 'waiting' WHERE user_id=?", [user_id]).fetchall()
            return id

def add_wait(time, user_id, text):
    with sqlite3.connect(path_to_db) as db:
        db.execute("INSERT INTO waiting "
                   "(dates, user_id, text) "
                   "VALUES (?, ?, ?)",
                   [time, int(user_id), text])
        db.commit()
        id = db.execute(f"SELECT rowid FROM 'waiting' WHERE user_id=?", [user_id]).fetchall()
        db.commit()
        return id

def update_money(user_id, money):
    with sqlite3.connect(path_to_db) as db:
        db.execute(f"UPDATE 'storage_users' SET balance=? WHERE user_id=?", [money, user_id])
        db.commit()
        return True


def add_userx(user_id, balance):
    with sqlite3.connect(path_to_db) as db:
        db.execute("INSERT INTO storage_users "
                   "(user_id, balance) "
                   "VALUES (?, ?)",
                   [user_id, int(balance)])
        db.commit()

# Путь к БД
path_to_db = "data/botBD.sqlite"

con = sqlite3.connect('data/bot.db')
cur = con.cursor()


def update_status(user_id, status_will, status_was):
    with sqlite3.connect(path_to_db) as db:
        db.execute(f"UPDATE 'storage_users' SET status=? WHERE user_id=? AND status=?", [status_will, user_id, status_was])
        db.commit()

def delete_status(user_id):
    with sqlite3.connect(path_to_db) as db:
        db.execute(f"DELETE FROM 'storage_users' WHERE user_id=? AND status=? OR status=?", [user_id, 0, 1])
        db.commit()


def check_status(user_id):
    with sqlite3.connect(path_to_db) as db:
        textik = ((db.execute(f"SELECT message_text FROM 'storage_users' WHERE user_id=? AND status=?", [user_id, 1])).fetchall())[0][0]
        print(textik)
        return textik

def create_bdx():
    with sqlite3.connect(path_to_db) as db:
        # Создание БД с хранением данных пользователей
        check_sql = db.execute("PRAGMA table_info(storage_users)")
        check_sql = check_sql.fetchall()
        check_create_users = [c for c in check_sql]
        if len(check_create_users) == 3:
            print("DB was found(1/9)")
        else:
            db.execute("CREATE TABLE storage_users("
                       "increment INTEGER PRIMARY KEY AUTOINCREMENT,"
                       "user_id INTEGER, balance INTEGER)")
            print("DB was not found(1/9) | Creating...")
        if len(check_create_users) == 3:
            print("DB was found(1/9)")
        else:
            db.execute("CREATE TABLE waiting("
                       "dates TIMESTAMP, user_id INTEGER, text TEXT)")
            print("DB was not found(1/9) | Creating...")

        print(len(check_create_users))
        if len(check_create_users) == 3:
            print("DB was found(1/9)")
        else:
            db.execute("CREATE TABLE all_answer("
                       "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                       "dates TIMESTAMP, user_id INTEGER, text TEXT,"
                       "answers TEXT, balance INTEGER)")
            print("DB was not found(1/9) | Creating...")
        db.commit()    