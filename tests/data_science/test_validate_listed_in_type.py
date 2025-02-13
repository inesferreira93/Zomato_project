import pytest
from pytest_bdd import scenarios, given, when, then
import config as configs
scenarios("../../features/data_science/validate_listed_in_type.feature")

@pytest.fixture(scope='function')
def context():
    return {}

@given("the database contains restaurant data")
def setup_database(database):
    """Fixture configured in conftest.py file"""
    pass

@when("I query the unique values of the 'listed_in_type' column")
def query_unique_values(database, context):
    conn, cursor = database
    column_name = "listed_in_type"
    cursor.execute(
        f"SELECT distinct {column_name} from ({configs.ZOMATO_TABLE['TABLE_NAME']}) "
        f"where {column_name} NOT IN ('Cafes', 'Buffet', 'Dining', 'other')"
    )
    context['rows'] = len(cursor.fetchall())

@then("all values must be 'Cafes', 'Buffet', 'Dining', or 'Other'")
def validate_values(context):
    assert context['rows'] == 0, f"Invalid values found: {len(context)}"