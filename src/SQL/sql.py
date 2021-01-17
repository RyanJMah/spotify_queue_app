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
"""
def delete_queue(song_name, db = connect()):

    cursor = db.cursor()
    sql = f"DELETE FROM 'queues' WHERE 'song_name' = {song_name}"
    cursor.execute(sql)
    db.commit()
    db.close()
    return
"""
def read_queue(db = connect()):
    df = pd.read_sql("SELECT * FROM queues", db)
    db.close()
    return df

def add_queue(guest_user, host_user, song_name, artist_name, time, db = connect()):
    cursor = db.cursor()
    sql = "INSERT INTO queues(guest_user, host_user, song_name, artist_name, time) VALUES (%s, %s, %s, %s, %s)"
    val = (guest_user, host_user, song_name, artist_name, time)
    cursor.execute(sql,val)
    db.commit()

    db.close()

def del_queue(db = connect()):
    pass

if __name__ == "__main__":
    #add_queue('3','urmom','garbage','everyday bro','1111-11-11')
    print(read_queue())