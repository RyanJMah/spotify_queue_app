import os
import sys
import mysql.connector
from credentials import *
import pandas as pd
import credentials as *


THIS_DIR = os.path.abspath(os.path.dirname(__file__))
PARENT_DIR = os.path.dirname(THIS_DIR)
sys.path.append(PARENT_DIR)


def delete_song(song_name):
    db = mysql.connector.connect(
        host = "MARIADB_HOST",
        user = "MARIADB_USER", 
        password = "MARIADB_PASSWORD",
        database = "MARIADB_DATABASE"
    )
    cursor = db.cursor()
    sql = f"DELETE FROM 'queues' WHERE 'song_name' = {song_name}"
    cursor.execute(sql)
    db.commit()
    db.close()
    return




def connect():
    db = mysql.connector.connect(
<<<<<<< HEAD
        host = "MARIADB_HOST",
        user = "MARIADB_USER", 
        password = "MARIADB_PASSWORD",
        database = "MARIADB_DATABASE"
    )
=======
            host = MARIADB_HOST,
            user = MARIADB_USER,
            password = MARIADB_PASSWORD,
            database = MARIADB_DATABASE
        )
    return db

def read_queue(db = connect()):
    df = pd.read_sql("SELECT * FROM queues", db)
>>>>>>> 0cced7a1dc2dd7dc1723bd038c4f2575e698a5e4
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

if __name__ == "__main__":
    add_queue('test','test','test','test','0000-00-00')
    print(read_queue())
