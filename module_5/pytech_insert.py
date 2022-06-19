""" 
Assignment: pytech_insert.py
Julia Delightly
Professor Sampson
19 June 2022
Description: Test program for inserting new documents into student collection
"""

# import statements
from pymongo import MongoClient

# MongoDB connection string 
url = "mongodb+srv://admin:admin@cluster0.kdyeb.mongodb.net/?retryWrites=true&w=majority"

# connect to MongoDB cluster 
client = MongoClient(url)

# connect pytech database
db = client.pytech

# student documents
mason = {
    "student_id": "1007",
    "first_name": "Mason",
    "last_name": "Bergenholtz",
    "enrollments": [
        {
            "term": "Session 1",
            "gpa": "3.5",
            "start_date": "March 14, 2022",
            "end_date": "May 15, 2022",
            "courses": [
                {
                    "course_id": "CSD200",
                    "description": "Foundation of Software Development",
                    "instructor": "Professor Sampson",
                    "grade": "A"
                },
                {
                    "course_id": "CSD205",
                    "description": "Intro to Programming with Python",
                    "instructor": "Professor Payne",
                    "grade": "B"
                }
            ]
        }
    ]

}

 
alyssum = {
    "student_id": "1008",
    "first_name": "Alyssum",
    "last_name": "Guerrero",
    "enrollments": [
        {
            "term": "Session 1",
            "gpa": "4.0",
            "start_date": "March 14, 2022",
            "end_date": "May 15, 2022",
            "courses": [
                  {
                    "course_id": "CSD200",
                    "description": "Foundation of Software Development",
                    "instructor": "Professor Sampson",
                    "grade": "A"
                },
                {
                    "course_id": "CSD205",
                    "description": "Intro to Programming with Python",
                    "instructor": "Professor Payne",
                    "grade": "A"
                }
            ]
        }
    ]
}


hannah = {
    "student_id": "1009",
    "first_name": "Hannah",
    "last_name": "Wiser",
    "enrollments": [
        {
            "term": "Session 1",
            "gpa": "2.5",
            "start_date": "March 14, 2022",
            "end_date": "May 15, 2022",
            "courses": [
                  {
                    "course_id": "CSD200",
                    "description": "Foundation of Software Development",
                    "instructor": "Professor Sampson",
                    "grade": "B"
                },
                {
                    "course_id": "CSD205",
                    "description": "Intro to Programming with Python",
                    "instructor": "Professor Payne",
                    "grade": "C"
                }
            ]
        }
    ]
}

# get the students collection and make a list of students
students = db.students
students_list = [mason, alyssum, hannah]

# insert statements and output 
print("\n  -- INSERT STATEMENTS --")
mason_student_id = students.insert_one(mason).inserted_id
print(f'Inserted student record {mason["first_name"]} {mason["last_name"]} into the students collection with document_id {mason_student_id}')

alyssum_student_id = students.insert_one(alyssum).inserted_id
print(f'Inserted student record {alyssum["first_name"]} {alyssum["last_name"]} into the students collection with document_id {alyssum_student_id}')

hannah_student_id = students.insert_one(hannah).inserted_id
print(f'Inserted student record {hannah["first_name"]} {hannah["last_name"]} into the students collection with document_id {hannah_student_id}')