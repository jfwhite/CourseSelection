import sqlite3
import json

# Connect to database
conn = sqlite3.connect("courses.db")
c = conn.cursor()

# Open data file
f = open("courses.json")
j = json.load(f)

# Prepare useful constants
STEM = ["MAT", "PHY", "MOL", "EEB", "CBE", "ELE", "COS", "CHM", "MAE", "AST", "CEE", "ORF", "SML"] 
HUM = ["POR", "LAT", "CLA", "HUM", "ENG", "HIS", "PHI", "MUS", "SLA", "COM", "AAS", "SPA", "PER"]
term = "1182"

# Process JSON to add a course to coursedata table
def insert_course(course):
    cid = course["courseid"]
    if cid in ids:
        return # don't duplicate courses, violating PRIMARY KEY constraint
    dim1 = get_dim1(course) # course level 
    dim2 = get_dim2(course) # course STEM-ness, currently sketchy
    dim3 = get_dim3(course) # course enrollment
    statement = "INSERT INTO coursedata VALUES ('{id}', {d1}, {d2}, {d3})"
    c.execute(statement.format(id = cid, d1 = dim1, d2 = dim2, d3 = dim3))
    ids.append(cid) # add to list of "visited" courseids

# Extract the course level
def get_dim1(course):
    if course.get("listings"):
        return int(course.get("listings")[0]["number"])
    else:
        return -1 # missing data

# Extract the course STEM-ness
def get_dim2(course):
    if course.get("listings"):
        if course.get("listings")[0]["dept"] in STEM:
            return 30 # very STEM
        elif course.get("listings")[0]["dept"] in HUM:
            return 10 # very non-STEM
        else:
            return 20 # in between: social sciences and other
    else:
        return -1 # missing data

# Extract the enrollment
def get_dim3(course):
    if course.get("classes"):
        return int(course["classes"][0]["enroll"])
    else:
        return -1 # missing data

# Initialize list of "visited" courseids
c.execute("SELECT CIDS FROM COURSEDATA")
ids = [row[0] for row in c.fetchall()]

# Process courses.json and use it to fill courses.db
for course in j:
    insert_course(course)

# Close database connection
conn.commit()
conn.close()
