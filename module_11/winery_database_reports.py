""" 
Assignment: winery_database_reports.py
Green Team: Kendrick Baker, Julia Delightly, Elizabeth Fung, Christopher Morales, Abigail Sabelhaus
Professor Sampson
17 July 2022
Description: Bacchus Winery Case Study Database Reports
"""

import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="winery_employee",
  password="JKD@sql22!",
  database="winery"
)

cursor = db.cursor()