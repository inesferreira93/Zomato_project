import pytest
from pytest_bdd import scenarios, given, when, then
import config as configs
scenarios("../../features/data_science/validate_rate_column.feature")

@pytest.fixture(scope='function')
def context():
    return {}

@given("the database contains restaurant data")
def setup_database(database):
    """Fixture configured in conftest.py file"""
    pass

@when("I query the values of the 'rate' column")
def query_unique_values(database, context):
    conn, cursor = database
    column_name = "rate"
    cursor.execute(f'select {column_name} from {configs.ZOMATO_TABLE['TABLE_NAME']} WHERE {column_name} NOT LIKE "%/5";')
    context['rows'] = len(cursor.fetchall())

@then("all values must be in the 'X/X' format")
def validate_values(context):
    assert context['rows'] == 0, f"Invalid values found: {len(context)}"