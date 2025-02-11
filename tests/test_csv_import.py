import csv
from config import TABLE_NAME

def test_csv_import(database):
    """Testing the data from CSB was imported to the DB"""
    conn, cursor = database
    csv_file_path = "./dataset/zomato.csv"

    # Importing the CSV to DB
    from services.csv_importer import import_csv_to_db
    import_csv_to_db(csv_file_path, conn, cursor) 

    # Reading data from DB
    cursor.execute(f"SELECT * FROM {TABLE_NAME}")
    db_rows = cursor.fetchall()

    # Reading the data from CSV
    with open(csv_file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        csv_data = [
            (
                row['name'],
                row['online_order'],
                row['book_table'],
                row['rate'],
                int(row['votes']),
                int(row['approx_cost(for two people)']),
                row['listed_in(type)']
            )
            for row in reader
        ]

    # Make sure the column data is the same that csv file
    assert db_rows == csv_data