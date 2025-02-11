import csv
import config as configs
from utils.csv_utils import extract_restaurant_data 

def test_csv_import(database):
    """Testing the data from CSB was imported to the DB"""
    conn, cursor = database
    csv_file_path = configs.CSV_FILE_PATH

    # Importing the CSV to DB
    from services.csv_importer import import_csv_to_db
    import_csv_to_db(csv_file_path, conn, cursor) 

    # Reading data from DB
    cursor.execute(f"SELECT * FROM {configs.ZOMATO_TABLE["TABLE_NAME"]}")
    db_rows = cursor.fetchall()

    # Reading the data from CSV
    with open(csv_file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        csv_data = [extract_restaurant_data(row) for row in reader]

    # Make sure the column data is the same that csv file
    assert db_rows == csv_data