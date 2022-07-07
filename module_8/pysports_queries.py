""" 
Assignment: pysports_queries.py
Julia Delightly
Professor Sampson
3 July 2022
Description: Test program to query MySQL database tables through the terminal window and a Python program
"""
import mysql.connector
from mysql.connector import errorcode

config = {
    "user" : "Julia",
    "password" : "JKD@sql22!",
    "host" : "127.0.0.1",
    "database" : "pysports",
    "raise_on_warnings" : True,
}

try:
    db = mysql.connector.connect(**config)

    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    input("\n\n Press any key to continue...")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")

    else:
        print(err)

cursor = db.cursor()

print()
print("-- DISPLAYING TEAM RECORDS --")

cursor.execute("SELECT team_id, team_name, mascot FROM team;")
teams = cursor.fetchall()

for team in teams:
    print("Team ID: {}".format(team[0]))
    print("Team Name: {}".format(team[1]))
    print("Mascot: {}".format(team[2]))
    print()


print("-- DISPLAYING PLAYER RECORDS --")

cursor.execute("SELECT player_id, first_name, last_name, team_id FROM player")
players = cursor.fetchall()


for player in players:
    print("Player ID: {}".format(player[0]))
    print("First Name: {}".format(player[1]))
    print("Last Name: {}".format(player[2]))
    print("Team ID: {}".format(player[3]))
    print()

input("\n\nPress any key to continue...")


db.close()