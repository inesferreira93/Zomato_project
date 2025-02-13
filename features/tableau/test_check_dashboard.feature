Feature: Open the page and check the dashboards

  Scenario: Open the page and check the dashboards
    Given open the page and reject the cookies
    When the page is built
    Then a title is shown
    And the body are shown
    And check the top 5 of the Job Role
