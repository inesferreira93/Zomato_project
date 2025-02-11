def extract_restaurant_data(row):
    return (
        row['name'],
        row['online_order'],
        row['book_table'],
        row['rate'],
        int(row['votes']),
        int(row['approx_cost(for two people)']),
        row['listed_in(type)']
    )