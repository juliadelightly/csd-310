""" 
Assignment: pytech_queries.py
Julia Delightly
Professor Sampson
19 June 2022
Description: Test program for querying student collection
"""

# import statements 
from pymongo import MongoClient

# MongoDB connection string 
url = "mongodb+srv://admin:admin@cluster0.kdyeb.mongodb.net/?retryWrites=true&w=majority"

# connect to the MongoDB cluster 
client = MongoClient(url)

# connect pytech database
db = client.pytech 

students = db.students 
student_list = students
student_docs = student_list.find({})

# print header
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

# loop through collection and print results 
for doc in student_docs:
    print(f'Student ID: {doc["student_id"]}')
    print(f'First Name: {doc["first_name"]}')
    print(f'Last Name: {doc["last_name"]}')
    print()


# find document by student_id
alyssum = students.find_one({"student_id": "1008"})

# print results 
print("\n-- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY --")
print("  Student ID: " + alyssum["student_id"] + "\n  First Name: " + alyssum["first_name"] + "\n  Last Name: " + alyssum["last_name"] + "\n")

# exit message 
input("\n\n  End of program, press any key to continue...")