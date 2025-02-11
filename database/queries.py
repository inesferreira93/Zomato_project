import os
import sqlite3

def get_connection(database_name):
    """ Returns a connection with DB (if doesn't exists) """
    os.makedirs(os.path.dirname(database_name), exist_ok=True)
    
    return sqlite3.connect(database_name)