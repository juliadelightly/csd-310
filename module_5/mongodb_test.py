from pymongo import MongoClient
 
try:
    conn = MongoClient()
    print("Connected successfully!!!")
except: 
    print("Could not connect to MongoDB")

# mongodb atlas url to connect python to mongodb using pymongo
url = "mongodb+srv://admin:admin@cluster0.kdyeb.mongodb.net/?retryWrites=true&w=majority"

db = conn.pytech

students = db.students
