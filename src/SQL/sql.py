import mysql.connector
import pandas as pd


if __name__ == "__main__":

    db = mysql.connector.connect(
            host = "",
            user = "admin",
            password = "",
            database = ""
        )
    db.close()
