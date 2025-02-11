import config as configs

def test_type_od_listed(database):
    """Testing of type of the listed"""
    conn, cursor = database
    column_name = "listed_in_type"

    # Reading data from DB
    cursor.execute(f"SELECT distinct {column_name} from ({configs.ZOMATO_TABLE["TABLE_NAME"]}) where {column_name} NOT IN ('Cafes', 'Buffet', 'Dining', 'other')")
    rows = cursor.fetchall()

    assert len(rows) == 0, f"Invalid values founded: {rows}"

    conn.close

def test_type_of_rate(database):
    """Testing of types of rate"""
    conn, cursor = database
    column_name = "rate"
    
    cursor.execute(f'select {column_name} from {configs.ZOMATO_TABLE["TABLE_NAME"]} WHERE {column_name} NOT LIKE "%/5";')
    rows = cursor.fetchall()
    
    assert len(rows) == 0, f"Invalid values founded: {rows}"

    conn.close