Feature: Validation of the 'rate' column  
  As a QA Engineer  
  I want to ensure that the 'rate' column contains only values in the "X/X" format  
  To maintain data integrity in the database  

  Scenario: Verify the format of values in the 'rate' column
    Given the database contains restaurant data
    When I query the values of the 'rate' column
    Then all values must be in the 'X/X' format