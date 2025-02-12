import pytest
from pytest_bdd import scenarios, given, when, then
import csv
import config as configs
from utils.csv_utils import extract_restaurant_data 
scenarios("../../features/validate_csv_imported.feature")

csv_file_path = configs.CSV_FILE_PATH

@pytest.fixture(scope='function')
def context():
    return {}

@given("the csv file")
def setup_database(database):
    """Fixture configured in conftest.py file"""
    pass

@when("importing to database")
def query_unique_values(database, context):
    conn, cursor = database
    # Importing the CSV to DB
    from services.csv_importer import import_csv_to_db
    import_csv_to_db(csv_file_path, conn, cursor) 
    # Reading data from DB
    cursor.execute(f"SELECT * FROM {configs.ZOMATO_TABLE["TABLE_NAME"]}")
    context['data'] = cursor.fetchall()

@then("all values from CSV file must be imported to DB")
def validate_values(context):
    # Reading the data from CSV
    with open(csv_file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        csv_data = [extract_restaurant_data(row) for row in reader]
    # Make sure the column data is the same that csv file
    assert context['data'] == csv_data