import sqlite3, os, pytest
from config import ZOMATO_TABLE
from dotenv import load_dotenv
from selenium import webdriver
from pathlib import Path
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from utils.csv_utils import take_screenshot 

env_path = Path(__file__).resolve().parent.parent / "env" / ".env"
load_dotenv(env_path)
test_db_path = "tests/test_data/test_restaurants.db"

@pytest.fixture(scope="session")
def database():
    if os.path.exists(test_db_path):
        os.remove(test_db_path)

    """Creating a dabatase to test"""
    
    # Create the folder if it doesn't exists
    os.makedirs(os.path.dirname(test_db_path), exist_ok=True)
    
    # Connecting to the DB
    conn = sqlite3.connect(test_db_path)
    cursor = conn.cursor()

    cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS {ZOMATO_TABLE["TABLE_NAME"]} (
        name TEXT,
        online_order TEXT,
        book_table TEXT,
        rate TEXT,
        votes INTEGER,
        approx_cost_for_two_people INTEGER,
        listed_in_type TEXT
    );
    ''')

    yield conn, cursor
    conn.close()


def get_driver(headless=True):
    # Configure the chrome options
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--headless=new") 
    chrome_options.add_argument("--window-size=1920,1080")
    
    # avoid the automation detection
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])

    service = Service(ChromeDriverManager().install())
    # Adding the headless mode, if necessary
    if headless:
        chrome_options.add_argument("--headless=new") 
    # Initialize the Webdriver with the option configured
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

@pytest.fixture
def setup_driver():
    try:
        driver = get_driver(os.getenv("HEADLESS")) # get the headless mode
        yield driver
        driver.quit()
    except Exception as e:
        take_screenshot(driver, "text_example_failure")
        raise e

@pytest.fixture
def base_url():
    return "https://public.tableau.com/app/profile/pradeepkumar.g/viz/HRAttritionDashboardRWFD_16570446563570/viz"

