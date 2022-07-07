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

def show_players(cursor, title):

    # inner join query 
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id ORDER BY player_id, first_name, last_name, team_name DESC")
    players = cursor.fetchall()

    print("\n  -- {} --".format(title))
    
    # iterate over player data set and display results 
    for player in players:
        print("  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team Name: {}\n".format(player[0], player[1], player[2], player[3]))

try:

    db = mysql.connector.connect(**config) 
    cursor = db.cursor()

    # insert player query 
    add_player = ("INSERT INTO player(first_name, last_name, team_id)"
                 "VALUES(%s, %s, %s)")
 
    player_data = ("Smeagol", "Shire Folk", 1)

    # insert new player record
    cursor.execute(add_player, player_data)

    db.commit()
 
    show_players(cursor, "DISPLAYING PLAYERS AFTER INSERT")

    # update new record 
    update_player = ("UPDATE player SET team_id = 2, first_name = 'Gollum', last_name = 'Ring Stealer' WHERE first_name = 'Smeagol'")

    cursor.execute(update_player)

    show_players(cursor, "DISPLAYING PLAYERS AFTER UPDATE")

    # delete query 
    delete_player = ("DELETE FROM player WHERE first_name = 'Gollum'")

    cursor.execute(delete_player)

    show_players(cursor, "DISPLAYING PLAYERS AFTER DELETE")


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