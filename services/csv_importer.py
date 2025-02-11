import csv
from config import ZOMATO_TABLE
from utils.csv_utils import extract_restaurant_data

def import_csv_to_db(csv_file_path, conn, cursor):
    """Importa dados de um arquivo CSV para o banco de dados."""
    # Reading the CSV file
    with open(csv_file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data = extract_restaurant_data(row)
            cursor.execute(f'''
            INSERT INTO {ZOMATO_TABLE["TABLE_NAME"]} {ZOMATO_TABLE["COLUMNS"]}
            VALUES (?, ?, ?, ?, ?, ?, ?);
            ''', data)

    conn.commit()