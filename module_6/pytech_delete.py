""" 
Assignment: pytech_delete.py
Julia Delightly
Professor Sampson
26 June 2022
Description: Test program for deleting documents in Pytech database
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
student_list = students.find({}) 

print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

# loop through current collection 
for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

# add temp document 
temp_doc = {
    "student_id": "1010",
    "first_name": "Nick",
    "last_name": "Jonas"
}

# insert temp_doc into MongoDB atlas 
temp_doc_id = students.insert_one(temp_doc).inserted_id

print("\n  -- INSERT STATEMENTS --")
print("  Inserted student record " + temp_doc["student_id"] + " into the students collection with document_id " + str(temp_doc_id))

# find all students in updated collection 
new_student_list = students.find({})

print("\n  -- DISPLAYING NEW STUDENT LIST DOC -- ")
# loop through updated collection with the new student doc and output results 
for doc in new_student_list: 
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

# call delete_one method to remove student_temp_doc
deleted_student_temp_doc = students.delete_one({"student_id": "1010"})

# find all students in collection with student_temp_doc now deleted
new_student_list = students.find({})

print("\n  -- DELETED STUDENT ID: 1010 --")

# loop through collection and output results 
for doc in new_student_list: 
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

# exit message 
input("\n\n  End of program, press any key to continue...")
