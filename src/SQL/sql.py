import mysql.connector
import pandas as pd


if __name__ == "__main__":

    db = mysql.connector.connect(
            host = "34.94.124.216",
            user = "admin",
            password = "password",
            database = "Database"
        )
    db.close()
