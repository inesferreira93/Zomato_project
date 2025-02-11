import csv
from config import TABLE_NAME

def import_csv_to_db(csv_file_path, conn, cursor):
    """Importa dados de um arquivo CSV para o banco de dados."""
    # Reading the CSV file
    with open(csv_file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            cursor.execute(f'''
            INSERT INTO {TABLE_NAME} (name, online_order, book_table, rate, votes, approx_cost_for_two_people, listed_in_type)
            VALUES (?, ?, ?, ?, ?, ?, ?);
            ''', (
                row['name'],
                row['online_order'],
                row['book_table'],
                row['rate'],
                int(row['votes']),
                int(row['approx_cost(for two people)']),
                row['listed_in(type)']
            ))

    conn.commit()