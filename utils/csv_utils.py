import os 

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

def take_screenshot(driver, test_name):
    screenshot_dir = "screenshots"
    os.makedirs(screenshot_dir, exist_ok=True)
    screenshot_path = os.path.join(screenshot_dir, f"{test_name}.png")
    driver.save_screenshot(screenshot_path)
    print(f"Screenshot saved at {screenshot_path}")