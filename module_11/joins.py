""" 
Assignment: winery_database_reports.py
Green Team: Kendrick Baker, Julia Delightly, Elizabeth Fung, Christopher Morales, Abigail Sabelhaus
Professor Sampson
17 July 2022
Description: Bacchus Winery Case Study Database Reports
"""

import mysql.connector
from datetime import datetime

#print date for when reports were run 
print()
now = datetime.now() # current date and time
date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
print("Report run on: ",date_time)
print()
print()



mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="winery_employee",
  password="JKD@sql22!",
  database="winery"
)




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


cursor = mydb.cursor()
# Report 1 to show the delivery gaps.
cursor.execute("SELECT delivery_metrics.month, suppliers.supplier_name, delivery_metrics.expected_deliverytime, delivery_metrics.actual_deliverytime, delivery_metrics.delivery_gap  FROM delivery_metrics INNER JOIN suppliers ON suppliers.supplier_id = delivery_metrics.supplier_id ORDER BY month DESC;")

response = cursor.fetchall()
print("Delivery Gaps by Month")
printTable(response,cursor)

# Report 2 to show which wine is selling the best, which isn't selling as well and what distributor carries which wine.
cursor.execute("SELECT wine.name, distributor.units, distributor.distributor_name FROM wine INNER JOIN distributor ON wine.upc = distributor.upc ORDER BY name DESC;")

response = cursor.fetchall()
print("Wine sales by distributor:")
printTable(response,cursor)

# Report 3 Showing how many hours an employee worked per quarter.
cursor.execute("SELECT time_sheet.time_worked, time_sheet.quarter, employee.last_name, employee.first_name FROM time_sheet INNER JOIN employee ON time_sheet.employee_id = employee.employee_id ORDER BY quarter;")

response = cursor.fetchall()
print("Employee Time by Time Worked")
printTable(response, cursor)

