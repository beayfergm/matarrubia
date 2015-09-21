#!/usr/bin/env python
# 
# Udacity Nanodegree: Fullstack Web Developer
# File: tournament.py -- implementation of a Swiss-system tournament
# Author: Fernando Matarrubia

import psycopg2
import bleach

def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def executeQuery(databaseCursor, query, listOfParameters=()):
    """Convenience method to safely execute an sql query"""
    if databaseCursor is None:
        raise TypeError("psql database cursor cannot be None.")

    # Using this phyton's formatting prevents sql injection attacks
    databaseCursor.execute(query, listOfParameters);


def deleteMatches():
    """Remove all the match records from the database."""
    databaseConnection = connect();
    databaseCursor = databaseConnection.cursor();
    query = "DELETE FROM matches;";
    executeQuery(databaseCursor, query);
    databaseConnection.commit();
    databaseConnection.close();


def deletePlayers():
    """Remove all the player records from the database."""
    databaseConnection = connect();
    databaseCursor = databaseConnection.cursor();
    query = "DELETE FROM players;";
    executeQuery(databaseCursor, query);
    databaseConnection.commit();
    databaseConnection.close();


def countPlayers():
    """Returns the number of players currently registered."""
    databaseConnection = connect();
    databaseCursor = databaseConnection.cursor();
    query = "SELECT count(*) as totalPlayers FROM players;";
    executeQuery(databaseCursor, query);
    result = databaseCursor.fetchall();
    databaseConnection.close();
    # Result value should be the first item in the first returned row
    totalPlayers = result[0][0];
    return totalPlayers;


def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    # Sanitizing the input before executing the query
    # This will escape or strip characters making the input safe and preventing sql injection attacks
    sanitizedName = bleach.clean(name);
    databaseConnection = connect();
    databaseCursor = databaseConnection.cursor();
    query = "INSERT INTO players (name) VALUES (%s);";
    executeQuery(databaseCursor, query, (sanitizedName,));
    databaseConnection.commit();
    databaseConnection.close();


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    databaseConnection = connect();
    databaseCursor = databaseConnection.cursor();
    query = "SELECT * FROM playerStandings;"
    executeQuery(databaseCursor, query);
    resultRows = databaseCursor.fetchall();
    databaseConnection.close();
    # Formatting output as a dictionary.
    playerStandings = [{'id': str(row[0]), 'name': str(row[1]), 'wins': row[2], 'matches': row[3]} for row in resultRows];
    return playerStandings;


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
 
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """


