import sqlite3

def get_connection(database_name):
    return sqlite3.connect(database_name)
/Users/ines/Repository/Zomato/database/connection.py