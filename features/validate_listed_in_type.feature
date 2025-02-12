Feature: Validation of the 'listed_in_type' column  
  As a QA Engineer  
  I want to ensure that the 'listed_in_type' column contains only allowed values  
  To maintain data integrity in the database  

  Scenario: Verify allowed values in the 'listed_in_type' column  
    Given the database contains restaurant data  
    When I query the unique values of the 'listed_in_type' column  
    Then all values must be 'Cafes', 'Buffet', 'Dining', or 'Other'