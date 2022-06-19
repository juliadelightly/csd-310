""" 
Assignment: mongodb_test.py
Julia Delightly
Professor Sampson
19 June 2022
Description: Test program for connecting to a MongoDB Atlas cluster
"""
# import statement
from pymongo import MongoClient

# MongoDB connection string 
url ="mongodb+srv://admin:admin@cluster0.kdyeb.mongodb.net/?retryWrites=true&w=majority"

# connect to MongoDB cluster 
client = MongoClient(url)

# connect pytech database
db = client.pytech

print("-- Pytech Collection List --")
print(db.list_collection_names())

# exit message 
input("\n\n  End of program, press any key to continue...")