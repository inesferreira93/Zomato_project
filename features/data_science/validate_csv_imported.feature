Feature: Validation of csv file imported to DB
  As a QA Engineer  
  I want to ensure that the csv file was imported to database without errors

  Scenario: Verify the database
    Given the csv file
    When importing to database
    Then all values from CSV file must be imported to DB