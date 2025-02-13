from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver

    def accept_cookies(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "onetrust-button-group"))
        )
        element.click()

    def wait_for_page_load(self):
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(), 'HR Attrition')]"))
        )

    def get_dashboard_title(self):
        title = self.driver.find_element(By.CSS_SELECTOR, "[class^='_title_'] h1")
        return title.text

    def switch_to_dashboard_iframe(self):
        iframe = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#embedded-viz-wrapper iframe"))
        )
        self.driver.switch_to.frame(iframe)

    def job_role_combo(self):
        dashboard_viewport = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "tabZoneId67"))
        )
        combo = WebDriverWait(dashboard_viewport, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "span[role='button']"))
        )
        return combo
    
    def waitForClicacleAndClick(self):
        combo_box_button = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'span[role="button"]'))
        )
        combo_box_button.click()
    

    def get_job_role_combo_text(self):
        combo = self.job_role_combo()
        comboText = WebDriverWait(combo, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[class='tabComboBoxName']"))
        )
        return comboText.text

    def changeJobRole(self):
        new_option = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='All Roles']"))
        )
        new_option.click()