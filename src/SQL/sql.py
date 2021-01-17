import os
import sys
import mysql.connector
from credentials import *
import pandas as pd

"""
THIS_DIR = os.path.abspath(os.path.dirname(__file__))
PARENT_DIR = os.path.dirname(THIS_DIR)
sys.path.append(PARENT_DIR)
"""

def connect():
    db = mysql.connector.connect(
            host = MARIADB_HOST,
            user = MARIADB_USER,
            password = MARIADB_PASSWORD,
            database = MARIADB_DATABASE
        )
    return db

def delete_queue(song_id, db = connect()):

    cursor = db.cursor()
    sql = f"DELETE FROM queues WHERE song_id = '{song_id}'"
    cursor.execute(sql)
    db.commit()
    db.close()
    return

def read_queue(db = connect(), q = None):
    if (q == None):
        df = pd.read_sql("SELECT * FROM queues", db)
    else:
        df = pd.read_sql(f"SELECT * FROM queues WHERE session_id = {q}", db)
    db.close()
    return df

def add_queue(session_id, guest_user, host_user, song_id, time, db = connect()):
    cursor = db.cursor()
    sql = "INSERT INTO queues(session_id, guest_user, host_user, song_id, time) VALUES (%s, %s, %s, %s, %s)"
    val = (session_id, guest_user, host_user, song_id, time)
    cursor.execute(sql,val)
    db.commit()

    db.close()

if __name__ == "__main__":
    #add_queue('5213','urmom','you','yah','2364-00-00')
    delete_queue('ram ranch')
    print(read_queue(q = 5213))
