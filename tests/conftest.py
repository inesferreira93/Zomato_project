import sqlite3, os, pytest
from config import ZOMATO_TABLE

test_db_path = "tests/test_data/test_restaurants.db"

@pytest.fixture(scope="session")
def database():
    if os.path.exists(test_db_path):
        os.remove(test_db_path)

    """Creating a dabatase to test"""
    
    # Create the folder if it doesn't exists
    os.makedirs(os.path.dirname(test_db_path), exist_ok=True)
    
    # Connecting to the DB
    conn = sqlite3.connect(test_db_path)
    cursor = conn.cursor()

    cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS {ZOMATO_TABLE["TABLE_NAME"]} (
        name TEXT,
        online_order TEXT,
        book_table TEXT,
        rate TEXT,
        votes INTEGER,
        approx_cost_for_two_people INTEGER,
        listed_in_type TEXT
    );
    ''')

    yield conn, cursor
    conn.close()
