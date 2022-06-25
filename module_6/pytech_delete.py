<<<<<<< HEAD
""" 
Assignment: pytech_delete.py
Julia Delightly
Professor Sampson
26 June 2022
Description: Test program for deleting documents in Pytech database
"""

# import statements
from pymongo import MongoClient #pymongo lets us interface with MongoDB

# MongoDB connection string 
url = "mongodb+srv://admin:admin@cluster0.lazzm.mongodb.net/pytech"

# connect to the MongoDB cluster 
client = MongoClient(url) #turns our connection string into a client we can interface

# connect pytech database
db = client.pytech
students = db.students
student_list = students.find({}) #without anything in {} returns all

print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

# loop through collection 
for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

# test document 
test_doc = {
    "student_id": "1010",
    "first_name": "John",
    "last_name": "Doe"
}

# insert test document into MongoDB atlas 
test_doc_id = students.insert_one(test_doc).inserted_id

# insert statements with output 
print("\n  -- INSERT STATEMENTS --")
print("  Inserted student record into the students collection with document_id " + str(test_doc_id))

# call find_one() method by student_id 1010
student_test_doc = students.find_one({"student_id": "1010"})

# display results 
print("\n  -- DISPLAYING STUDENT TEST DOC -- ")
print("  Student ID: " + student_test_doc["student_id"] + "\n  First Name: " + student_test_doc["first_name"] + "\n  Last Name: " + student_test_doc["last_name"] + "\n")

# call delete_one method to remove student_test_doc
deleted_student_test_doc = students.delete_one({"student_id": "1010"})

# find all students in collection 
new_student_list = students.find({})

print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

# loop through collection and output results 
for doc in new_student_list: 
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

# exit message 
input("\n\n  End of program, press any key to continue...")
=======

>>>>>>> 746522b67e792ef7aa05f96a8c375ffe802cfbfa
