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
    query = "SELECT * FROM playerStandings;";
    executeQuery(databaseCursor, query);
    resultRows = databaseCursor.fetchall();
    databaseConnection.close();
    playerStandings = [{'id': str(row[0]), 'name': str(row[1]), 'tournament': row[2], 'wins': row[3], 'matches': row[4]} for row in resultRows];
    return playerStandings;

def playerStandingsInTournament(tournamentId):
    """Returns a list of the players and their win records, sorted by wins and filtered by tournamentId

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
    query = "SELECT * FROM playerStandings WHERE tournament_id = (%s)";
    executeQuery(databaseCursor, query, (tournamentId,));
    resultRows = databaseCursor.fetchall();
    databaseConnection.close();
    playerStandings = [{'id': str(row[0]), 'name': str(row[1]), 'tournament': row[2], 'wins': row[3], 'matches': row[4]} for row in resultRows];
    return playerStandings;


def reportMatch(tournament, winner, loser, comments):
    """Records the outcome of a single match between two players.

    Args:
      tournament:  the id number of the tournament where the match took place in
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
      comments: string containing comments about the match
    """
    databaseConnection = connect();
    databaseCursor = databaseConnection.cursor();
    query = "INSERT INTO matches VALUES ((%s), (%s), (%s), (%s));";
    executeQuery(databaseCursor, query, (tournament, winner, loser, comments, ));
    databaseConnection.commit();
    databaseConnection.close();
 
def createPairs(list):
    """Generator function to return a list of pairs given an existing list

        Reference: https://www.jeffknupp.com/blog/2013/04/07/improve-your-python-yield-and-generators-explained/
    """
    listIterator = iter(list)
    # Yields on two values at a time and returns a tuple containing both of them
    while True:
        yield(listIterator.next(), listIterator.next())
 
def swissPairings(tournamentId = -1):
    """Returns a list of pairs of players for the next round of a match. A tournamentId is optional.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    If a tournament Id is specified, the pairing will be done between players with matches on a given tournament. 
    If no index is specified, the pairing will be done using all existing player standings, that is, taking in account
    results of all players in all tournaments
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    # Depending on the tournamentId we need to fetch the standings in a given way
    playerStandingsList = playerStandings() if (tournamentId == -1) else playerStandingsInTournament(tournamentId);
    # Then, we create the pairs using a generator function
    standingPairs = createPairs(playerStandingsList);
    # Finally we build the result with the required structure and return them
    result = [{'id1': pair[0]["id"], 'name1': str(pair[0]["name"]), 'id2': pair[1]["id"], 'name2': str(pair[1]["name"])} for pair in standingPairs];
    return result


