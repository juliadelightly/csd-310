""" 
Assignment: winery_database.py
Green Team: Kendrick Baker, Julia Delightly, Elizabeth Fung, Christopher Morales, Abigail Sabelhaus
Professor Sampson
10 July 2022
Description: Bacchus Winery Case Study Database
"""

import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="winery_employee",
  password="JKD@sql22!",
  database="winery"
)


mycursor = mydb.cursor()


#Inserting records into tables.
#Suppliers table
supplier_insert = "INSERT INTO suppliers (supplier_name) VALUES (%s)"
name1 = ('Wine Supplies')
name2 = ('Boxes and Things')
name3 =  ('Tubes R Us')

#Employee table
employee_insert = "INSERT INTO employee( first_name, last_name, job_Title) VALUES(%s,%s,%s)"
worker1 = ('Stan', 'Bacchus', 'Logistics Comanager')
worker2 = ('Davis','Bacchus', 'Logistics Comanager')
worker3 = ('Janet', 'Collins', 'Payroll')
worker4 = ('Roz', 'Murphy', 'Marketing')
worker5 = ('Bob', 'Ulrich', 'Assistant')
worker6 = ('Maria', 'Costanza', 'Distribution')

#Time_sheet table
time_sheet_insert= "INSERT INTO time_sheet(employee_id, time_worked, quarter) VALUES(%s,%s,%s)"
time_sheet1 = (1, '535 hours', 1)
time_sheet2 = (1,'518 hours', 2)
time_sheet3 = (1, '580 hours', 3)
time_sheet4 = (1, '550 hours', 4)
time_sheet5 = (2,'400 hours', 1)
time_sheet6 = (2, '433 hours', 2)

#Delivery_metrics table
metrics_insert = "INSERT INTO delivery_metrics(supplier_id, expected_deliverytime, actual_deliverytime, delivery_gap,month) VALUES(%s,%s, %s, %s,%s)"
delivery1 = (1,'12:00:00', '13:00:00', '01:00:00','April')
delivery2 = (2,'14:50:00', '14:55:00', '00:05:00','June')
delivery3 = (3,'10:35:00', '10:30:00', '00:05:00','September')
delivery4 = (1,'09:45:00', '09:00:00', '00:45:00','July')
delivery5 = (3,'06:00:00', '08:30:00', '02:30:00','April')
delivery6 = (2,'10:30:00', '10:30:00', '00:00:00','April')

#Wine table
wine_insert = "INSERT INTO wine(name , upc)VALUES(%s,%s)"
wine1 = ('Merlot', 100067)
wine2 = ('Cabernet', 200067)
wine3 = ('Chablis', 300067)
wine4 = ('Chardonnay', 400067)

#Distributor table
distributor_insert = "INSERT INTO distributor(order_id, distributor_name, pickup_time, units, upc ) VALUES(%s, %s, %s, %s,%s)"
distributor1 = (1012, 'Transparent_transport', '06:00:00', 60, 100067) 
distributor2 = (1013, 'Marthas_Movers', '01:00:00', 100 , 200067)
distributor3 = (1014, 'Dick&Sons', '16:30:00', 30, 200067)
distributor4 = (1015, 'St_Vincent_Deliveries_inc', '03:30:00', 100, 400067)
distributor5 = (1016, 'St_Vincent_Deliveries_inc', '03:45:00', 100, 300067)
distributor6 = (1017, 'St_Vincent_Deliveries_inc', '03:50:00', 100 , 100067)


#Executing supplier inserts
mycursor.execute(supplier_insert, (name1,))
mycursor.execute(supplier_insert, (name2,))
mycursor.execute(supplier_insert, (name3,))

#Executing employee inserts
mycursor.execute(employee_insert, (worker1))
mycursor.execute(employee_insert, (worker2))
mycursor.execute(employee_insert, (worker3))
mycursor.execute(employee_insert, (worker4))
mycursor.execute(employee_insert, (worker5))
mycursor.execute(employee_insert, (worker6))

#Executing time_sheet inserts
mycursor.execute(time_sheet_insert, (time_sheet1))
mycursor.execute(time_sheet_insert, (time_sheet2))
mycursor.execute(time_sheet_insert, (time_sheet3))
mycursor.execute(time_sheet_insert, (time_sheet4))
mycursor.execute(time_sheet_insert, (time_sheet5))
mycursor.execute(time_sheet_insert, (time_sheet6))

#Executing delivery_metrics inserts
mycursor.execute(metrics_insert, (delivery1))
mycursor.execute(metrics_insert, (delivery2))
mycursor.execute(metrics_insert, (delivery3))
mycursor.execute(metrics_insert, (delivery4))
mycursor.execute(metrics_insert, (delivery5))
mycursor.execute(metrics_insert, (delivery6))

#Executing wine inserts
mycursor.execute(wine_insert, (wine1))
mycursor.execute(wine_insert, (wine2))
mycursor.execute(wine_insert, (wine3))
mycursor.execute(wine_insert, (wine4))

#Executing distributor inserts
mycursor.execute(distributor_insert, (distributor1))
mycursor.execute(distributor_insert, (distributor2))
mycursor.execute(distributor_insert, (distributor3))
mycursor.execute(distributor_insert, (distributor4))
mycursor.execute(distributor_insert, (distributor5))
mycursor.execute(distributor_insert, (distributor6))


mydb.commit()



print("---Displaying Suppliers Records ---")
cursor = mydb.cursor()
cursor.execute("SELECT supplier_id, supplier_name FROM suppliers")
supplier = cursor.fetchall()
for suppliers in supplier:
   
    print("Supplier ID: {}".format(suppliers[0]))
    print("Supplier Name: {}".format(suppliers[1]))
    print("\n")


print("---Displaying Employee Records ---")
cursor = mydb.cursor()
cursor.execute("SELECT employee_id, first_name, last_name, job_title FROM employee")
employees = cursor.fetchall()
for employee in employees:
   
    print("Employee ID: {}".format(employee[0]))
    print("First Name: {}".format(employee[1]))
    print("Last Name: {}".format(employee[2]))
    print("Job Title: {}".format(employee[3]))
    print("\n")

print("---Displaying Time Sheet Records---")
cursor = mydb.cursor()
cursor.execute("SELECT employee_id, time_worked, quarter FROM time_sheet")
time_sheets = cursor.fetchall()
for time_sheet in time_sheets:
	print("Employee ID: {}".format(time_sheet[0]))
	print("Time Worked: {}".format(time_sheet[1]))
	print("Quarter: {}".format(time_sheet[2]))
	print("\n")

print("--- Displaying Delivery Metrics ---")
cursor = mydb.cursor()
cursor.execute("SELECT delivery_id, actual_deliveryTime, expected_deliveryTime, delivery_gap, supplier_id, month FROM delivery_metrics")
deliveries = cursor.fetchall()
for delivery_metrics in deliveries:
    print("Delivery ID: {}".format(delivery_metrics[0]))
    print("Actual Delivery Time: {}".format(delivery_metrics[1]))
    print("Expected Delivery Time: {}".format(delivery_metrics[2]))
    print("Delivery Gap: {}".format(delivery_metrics[3]))
    print("Supplier ID: {}".format(delivery_metrics[4]))
    print("Month: {}".format(delivery_metrics[5]))
    print("\n")

print("---Displaying Wine Records --- ")
mycursor = mydb.cursor()
mycursor.execute("SELECT  name , upc FROM wine")
wines = mycursor.fetchall()
for wine in wines:

  print("Wine : {}".format(wine[0]))
  print("UPC : {}".format(wine[1]))
  print("\n")


print("--- Displaying Distributor Records ---")
mycursor = mydb.cursor()
mycursor.execute("SELECT order_id, distributor_id, distributor_name, pickup_time, upc, units FROM distributor")
distributors = mycursor.fetchall()
for distributor in distributors:
    print("Order_ID: {}".format(distributor[0]))
    print("Distributor_Id: {}".format(distributor[1]))
    print("Distributor_Name: {}".format(distributor[2]))
    print("Pickup_Time: {}".format(distributor[3]))
    print("UPC: {}".format(distributor[4]))
    print("UPC: {}".format(distributor[5]))
    print("\n")