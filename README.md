# CourseSelection

Algorithm for choosing Princeton courses based on binary search

- courses.db is the database file. It stores the coursedata table.

- courses.json stores data about Spring '17 courses in JSON format

- create_table.py drops the old coursedata table and creates a new one

- insert_data.py fills the coursedata table with data from courses.json

- interact_with_user.py implements our course selection algorithm

#

Usage:

$ python create_table.py

$ python insert_data.py

$ python interact_with_user.py
