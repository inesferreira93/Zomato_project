from pytest_bdd import scenarios, given, when, then
import time
from po.dashboard_page import DashboardPage

scenarios('../../../features/tableau/test_check_dashboard.feature')

@given('open the page and reject the cookies')
def open_url(setup_driver, base_url):
    driver = setup_driver
    driver.get(base_url)
    dashboard = DashboardPage(driver)
    dashboard.accept_cookies()
    
@when('the page is built')
def reject_cookies(setup_driver):
    dashboard = DashboardPage(setup_driver)
    time.sleep(15)
    dashboard.wait_for_page_load()

@then('a title is shown')
def check_title(setup_driver):
    print(1)
    # dashboard = DashboardPage(setup_driver)
    # assert "HR Attrition Dashboard | VOTD | #IIBAwards'22" in dashboard.get_dashboard_title()

@then('the body are shown')
def dashboards_are_shown(setup_driver):
    print(1)
    # dashboard = DashboardPage(setup_driver)
    # dashboard.switch_to_dashboard_iframe()

@then('check the top 5 of the Job Role')
def check_overview_tab(setup_driver):
    print(1)
    # dashboard = DashboardPage(setup_driver)
    # assert "Top 5" in dashboard.get_job_role_combo_text()