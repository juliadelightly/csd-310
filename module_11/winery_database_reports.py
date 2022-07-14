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

cursor = mydb.cursor()

def printTable(results,cursor):
    """Prints table in MySQL format"""
    #source: https://stackoverflow.com/a/20383011
    widths = []
    columns = []
    tavnit = '|'
    separator = '+' 

    for column,cd in enumerate(cursor.description):
        width = len(cd[0])
        for rowNumber in range(len(response)):
            if len(str(response[rowNumber][column])) > width:
                width = len(str(response[rowNumber][column]))
        widths.append(width)
        columns.append(cd[0])

    for w in widths:
        tavnit += " %-"+"%ss |" % (w,)
        separator += '-'*w + '--+'

    print(separator)
    print(tavnit % tuple(columns))
    print(separator)
    for row in results:
        print(tavnit % row)
    print(separator)
    print()

cursor.execute("SELECT wine.name, distributor.units, distributor.distributor_name FROM wine INNER JOIN distributor ON wine.upc = distributor.upc ORDER BY units DESC;")

response = cursor.fetchall()
print("Wine sales by distributor:")
printTable(response,cursor)

cursor.execute()

response = cursor.fetchall()
print("Wine sales by total units:")
printTable(response,cursor)