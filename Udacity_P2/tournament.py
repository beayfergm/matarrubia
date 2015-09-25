#!/usr/bin/env python
# 
# Udacity Nanodegree: Fullstack Web Developer
# File: tournament.py -- implementation of a Swiss-system tournament
# Author: Fernando Matarrubia

import psycopg2
import contextlib

@contextlib.contextmanager
def get_cursor():
    """
    Helper function using the context lib to avoid repeating the same code when executing queries
    Reference: Udacity first project review
    Reference: https://docs.python.org/2/library/contextlib.html
    Reference: http://thecodeship.com/patterns/guide-to-python-function-decorators/
    """
    conn = connect()
    cur = conn.cursor()
    try:
        yield cur
    except:
        raise
    else:
        conn.commit()
    finally:
        cur.close()
        conn.close()

def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def executeQuery(query, fetchResults, listOfParameters=()):
    """Convenience method to safely execute an sql query"""
    results = None;
    with get_cursor() as cursor:
        # Using this phyton's formatting prevents sql injection attacks
        cursor.execute(query, listOfParameters);
        if (fetchResults):
            results = cursor.fetchall();
    return results;


def deleteMatches():
    """Remove all the match records from the database."""
    query = "DELETE FROM matches;";
    executeQuery(query, False);


def deletePlayers():
    """Remove all the player records from the database."""
    query = "DELETE FROM players;";
    executeQuery(query, False);


def deleteTournaments():
    """Remove all the tournament records from the database."""
    query = "DELETE FROM tournaments;";
    executeQuery(query, False);


def countPlayers():
    """Returns the number of players currently registered."""
    query = "SELECT count(*) as totalPlayers FROM players;";
    result = executeQuery(query, True);
    # Result value should be the first item in the first returned row
    totalPlayers = result[0][0];
    return totalPlayers;


def countTournaments():
    """Returns the number of tournaments currently registered."""
    query = "SELECT count(*) as totalTournaments FROM tournaments;";
    result = executeQuery(query, True);
    # Result value should be the first item in the first returned row
    totalTournaments = result[0][0];
    return totalTournaments;


def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    # Sanitizing the input before executing the query
    # This will escape or strip characters making the input safe and preventing sql injection attacks
    query = "INSERT INTO players (name) VALUES (%s);";
    executeQuery(query, False, (name,));


def registerTournament(name):
    """Adds a tournament to the tournament database.
  
    The database assigns a unique serial id number for the tournament.
  
    Args:
      name: the tournament's name (it doesn't need to be unique).
    """
    # Sanitizing the input before executing the query
    # This will escape or strip characters making the input safe and preventing sql injection attacks
    query = "INSERT INTO tournaments (name) VALUES (%s);";
    executeQuery(query, False, (name,));


def getTournaments():
    """Returns a list of the existing tournaments.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name):
        id: the tournament's unique id 
        name: the tournaments's name (as registered)
    """
    query = "SELECT * FROM tournaments;";
    result = executeQuery(query, True);
    tournaments = [[row[0], row[1]] for row in result];
    return tournaments;


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
    query = "SELECT id, name, wins, matches FROM playerStandings;";
    playerStandings = executeQuery(query, True);
    return playerStandings;


def playerStandingsInTournament(tournamentId):
    """Returns a list of the players and their win records, sorted by wins and filtered by tournamentId

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, tournament_id, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        tournament_id: the tournament's unique id
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    query = "SELECT * FROM playerStandings WHERE tournament_id = (%s)";
    playerStandings = executeQuery(query, True, (tournamentId,));
    return playerStandings;


def reportMatch(winner, loser, tournament=-1, comments=""):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
      tournament:  the id number of the tournament where the match took place in. 
                    If -1 the first tournament int he database will be use as default.
      comments: string containing comments about the match
    """
    # This code will use the first tournament in the database as the default tournament
    # when reporting a match with an invalid tournament id
    if(tournament == -1):
        tournaments = getTournaments()
        if (len(tournaments) == 0):
            raise ValueError("Cannot report a match if there are no tournaments in the databse")
            return
        else:
            tournament = tournaments[0][0];

    query = "INSERT INTO matches VALUES ((%s), (%s), (%s), (%s));";
    executeQuery(query, False, (tournament, winner, loser, comments, ));

 
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
    result = [[pair[0][0], str(pair[0][1]), pair[1][0], str(pair[1][1])] for pair in standingPairs];
    return result

