import os
import sys
import mysql.connector
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




if __name__ == "__main__":

    db = mysql.connector.connect(
        host = "MARIADB_HOST",
        user = "MARIADB_USER", 
        password = "MARIADB_PASSWORD",
        database = "MARIADB_DATABASE"
    )
    db.close()
