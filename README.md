## Zomato_project
### to activate the the venv in windows:
#### source venv/bin/activate
### no linux / macOs:
#### source venv/bin/activate

#### to Run the tests just need to run: 
##### ```pytest --bdd-report="report.html"``` OR ```pytest -s --bdd-report="report.html"``` (if you want to see the details) 
##### OR ```pytest -k <name_of_file>```, such as: ```pytest -k test_csv_import_to_db.py```