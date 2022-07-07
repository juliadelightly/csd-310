""" 
Assignment: pysports_join_queries.py
Julia Delightly
Professor Sampson
10 July 2022
Description: Test program to join the player and team tables
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
    cursor = db.cursor()

    # delete any existing versions of Smeagol from running this program with the update file more than once 
    cursor.execute("DELETE FROM player WHERE first_name = 'Smeagol';")

    # inner join query to return matching records
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")
    players = cursor.fetchall()

    print("\n  -- DISPLAYING PLAYER RECORDS --")
    
    # iterate over player data set and display results 
    for player in players:
        print("Player ID: {}".format(player[0]))
        print("First Name: {}".format(player[1]))
        print("Last Name: {}".format(player[2]))
        print("Team Name: {}".format(player[3]))
        print()

    input("\n\n  Press any key to continue... ")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:

    db.close()