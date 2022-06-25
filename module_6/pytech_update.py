<<<<<<< HEAD
""" 
Assignment: pytech_update.py
Julia Delightly
Professor Sampson
26 June 2022
Description: Test program for updating documents in Pytech database
"""

# import statements
from pymongo import MongoClient

# MongoDB connection string 
url = "mongodb+srv://admin:admin@cluster0.kdyeb.mongodb.net/?retryWrites=true&w=majority"

# connect to MongoDB cluster 
client = MongoClient(url)

# connect pytech database and find students in collection
db = client.pytech
students = db.students
student_list = students.find({})


print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

# loop through collection
for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

# update the student document using $set to change the value of last name
result = students.update_one({"student_id": "1007"}, {"$set": {"last_name": "Pankow"}})

# find updated student document 
mason = students.find_one({"student_id": "1007"})

# output updated document
print("\n  -- DISPLAYING STUDENT DOCUMENT 1007 --")
print("  Student ID: " + mason["student_id"] + "\n  First Name: " + mason["first_name"] + "\n  Last Name: " + mason["last_name"] + "\n")

# exit message 
input("\n\n  End of program, press any key to continue...")
=======

>>>>>>> 746522b67e792ef7aa05f96a8c375ffe802cfbfa
