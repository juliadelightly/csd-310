""" 
Assignment: pysports_update_and_delete.py
Julia Delightly
Professor Sampson
10 July 2022
Description: Program to test inserting, updating, and deleting records from pysports database
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

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")

    else:
        print(err)

# create a cursor
cursor = db.cursor()

# delete any existing versions of Smeagol from running this program more than once 
cursor.execute("DELETE FROM player WHERE first_name = 'Smeagol';")

# insert new player
cursor.execute("INSERT INTO player (first_name, last_name, team_id)\
VALUES('Smeagol', 'Shire Folk', 1)")

# inner join query 
cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id ORDER BY player_id;")
players = cursor.fetchall()


print()
print("-- DISPLAYING PLAYERS AFTER INSERT --")

for player in players:
    print("Player ID: {}".format(player[0]))
    print("First Name: {}".format(player[1]))
    print("Last Name: {}".format(player[2]))
    print("Team Name: {}".format(player[3]))
    print()

# update new player
cursor.execute("UPDATE player SET team_id = 2, first_name = 'Gollum', last_name = 'Ring Stealer' WHERE first_name = 'Smeagol'")

# join after update
cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id ORDER BY player_id;")
players = cursor.fetchall()

print()
print("-- DISPLAYING PLAYERS AFTER UPDATE --")


for player in players:
    print("Player ID: {}".format(player[0]))
    print("First Name: {}".format(player[1]))
    print("Last Name: {}".format(player[2]))
    print("Team Name: {}".format(player[3]))
    print()

# delete the new player
cursor.execute("DELETE FROM player WHERE first_name = 'Gollum';")

# join after delete
cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id ORDER BY player_id;")
players = cursor.fetchall()

print()
print("-- DISPLAYING PLAYERS AFTER DELETE --")

for player in players:
    print("Player ID: {}".format(player[0]))
    print("First Name: {}".format(player[1]))
    print("Last Name: {}".format(player[2]))
    print("Team Name: {}".format(player[3]))
    print()


input("\n\nPress any key to continue... ")
print()


db.close()
