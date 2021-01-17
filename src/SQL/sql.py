import mysql.connector
from credentials import *
import pandas as pd


def connect():
    db = mysql.connector.connect(
            host = MARIADB_HOST,
            user = MARIADB_USER,
            password = MARIADB_PASSWORD,
            database = MARIADB_DATABASE
        )
    return db

def read_queue(db = connect()):
    df = pd.read_sql("SELECT * FROM queues", db)
    db.close()
    return df

def add_queue(session_id, guest_user, host_user, song_id, time, db = connect()):
    cursor = db.cursor()
    sql = "INSERT INTO queues(session_id, guest_user, host_user, song_id, time) VALUES (%s, %s, %s, %s, %s)"
    val = (session_id, guest_user, host_user, song_id, time)
    cursor.execute(sql,val)
    db.commit()

    db.close()

#def del_queue(db = connect())

if __name__ == "__main__":
    add_queue('5214','test','test','test','0000-00-00')
    print(read_queue())
