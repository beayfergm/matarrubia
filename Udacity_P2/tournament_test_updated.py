#!/usr/bin/env python
#
# Test cases for tournament.py

from tournament import *

def testDeleteTournaments():
    deleteTournaments()
    print "0. Old tournaments can be deleted."


def testDeleteMatches():
    deleteTournaments()
    deleteMatches()
    print "1. Old matches can be deleted."


def testDelete():
    deleteTournaments()
    deleteMatches()
    deletePlayers()
    print "2. Player records can be deleted."


def testCount():
    deleteMatches()
    deletePlayers()
    c = countPlayers()
    if c == '0':
        raise TypeError(
            "countPlayers() should return numeric zero, not string '0'.")
    if c != 0:
        raise ValueError("After deleting, countPlayers should return zero.")
    print "3. After deleting, countPlayers() returns zero."


def testTournamentCount():
    deleteTournaments()
    deleteMatches()
    deletePlayers()
    c = countTournaments()
    if c == '0':
        raise TypeError(
            "countTournaments() should return numeric zero, not string '0'.")
    if c != 0:
        raise ValueError("After deleting, countTournaments should return zero.")
    print "4. After deleting, countTournaments() returns zero."


def testRegister():
    deleteMatches()
    deletePlayers()
    registerPlayer("Chandra Nalaar")
    c = countPlayers()
    if c != 1:
        raise ValueError(
            "After one player registers, countPlayers() should be 1.")
    print "5. After registering a player, countPlayers() returns 1."


def testRegisterTournament():
    deleteTournaments()
    deleteMatches()
    deletePlayers()
    registerTournament("Test Udacity Tournament")
    c = countTournaments()
    if c != 1:
        raise ValueError(
            "After registering one tournament, countTournaments() should be 1.")
    print "6. After registering one tournament, countTournaments() returns 1."


def testRegisterCountDelete():
    deleteTournaments()
    deleteMatches()
    deletePlayers()
    registerPlayer("Markov Chaney")
    registerPlayer("Joe Malik")
    registerPlayer("Mao Tsu-hsi")
    registerPlayer("Atlanta Hope")
    c = countPlayers()
    if c != 4:
        raise ValueError(
            "After registering four players, countPlayers should be 4.")
    deletePlayers()
    c = countPlayers()
    if c != 0:
        raise ValueError("After deleting, countPlayers should return zero.")
    print "7. Players can be registered and deleted."


def testRegisterCountDeleteTournaments():
    deleteTournaments()
    deleteMatches()
    deletePlayers()
    registerTournament("Test Udacity Tournament")
    registerTournament("Test Nanodegree Tournament")
    registerTournament("Test Online Learning Tournament")
    c = countTournaments()
    if c != 3:
        raise ValueError(
            "After registering three tournaments players, countTournaments should be 3.")
    deleteTournaments()
    c = countTournaments()
    if c != 0:
        raise ValueError("After deleting, countTournaments should return zero.")
    print "8. Tournaments can be registered and deleted."


def testStandingsBeforeMatches():
    deleteTournaments()
    deleteMatches()
    deletePlayers()
    registerPlayer("Melpomene Murray")
    registerPlayer("Randy Schwartz")
    standings = playerStandings()
    if len(standings) < 2:
        raise ValueError("Players should appear in playerStandings even before "
                         "they have played any matches.")
    elif len(standings) > 2:
        raise ValueError("Only registered players should appear in standings.")
    if len(standings[0]) != 4:
        raise ValueError("Each playerStandings row should have four columns.")
    [(id1, name1, wins1, matches1), (id2, name2, wins2, matches2)] = standings
    if standings[0][3] != 0 or standings[1][3] != 0 or standings[0][2] != 0 or standings[1][2] != 0:
        raise ValueError(
            "Newly registered players should have no matches or wins.")
    if set([standings[0][1], standings[1][1]]) != set(["Melpomene Murray", "Randy Schwartz"]):
        raise ValueError("Registered players' names should appear in standings, "
                         "even if they have no matches played.")
    print "9. Newly registered players appear in the standings with no matches."


def testStandingsBeforeMatchesWithTournament():
    deleteTournaments()
    deleteMatches()
    deletePlayers()
    registerPlayer("Melpomene Murray")
    registerPlayer("Randy Schwartz")
    registerTournament("Test Udacity Tournament")
    tournaments = getTournaments()
    tid = tournaments[0][0]
    standings = playerStandingsInTournament(tid)
    if len(standings) > 0:
        raise ValueError("Players should not appear in an specific tournament playerStandings "
                         "before having played any matches in that tournament.")
    print "10. Newly registered players do not appear in an specific tournament standings with no matches."


def testReportMatches():
    deleteTournaments()
    deleteMatches()
    deletePlayers()
    registerPlayer("Bruno Walton")
    registerPlayer("Boots O'Neal")
    registerPlayer("Cathy Burton")
    registerPlayer("Diane Grant")
    registerTournament("Test Udacity Tournament")
    tournaments = getTournaments()
    tid = tournaments[0][0]
    standings = playerStandings()
    [id1, id2, id3, id4] = [row[0] for row in standings]
    reportMatch(id1, id2, tid, 'Test Report Match 1')
    reportMatch(id3, id4, tid, 'Test Report Match 2')
    # The matches are created in tournament = tid, so we use that one for retrieving the new standings
    standings = playerStandingsInTournament(tid)
    for row in standings:
        i = row[0];
        m = row[4];
        w = row[3];
        if m != 1:
            raise ValueError("Each player should have one match recorded.")
        if i in (id1, id3) and w != 1:
            raise ValueError("Each match winner should have one win recorded.")
        elif i in (id2, id4) and w != 0:
            raise ValueError("Each match loser should have zero wins recorded.")
    print "11. After a match, players have updated standings."


def testPairings():
    deleteTournaments()
    deleteMatches()
    deletePlayers()
    registerPlayer("Twilight Sparkle")
    registerPlayer("Fluttershy")
    registerPlayer("Applejack")
    registerPlayer("Pinkie Pie")
    registerTournament("Test Udacity Tournament")
    tournaments = getTournaments()
    tid = tournaments[0][0]
    standings = playerStandings()
    [id1, id2, id3, id4] = [row[0] for row in standings]
    reportMatch(id1, id2, tid, 'Test Report Match 1')
    reportMatch(id3, id4, tid, 'Test Report Match 2')
    # The matches are created in tournament = tid, so we use that one for retrieving the new standings
    pairings = swissPairings(tid)
    if len(pairings) != 2:
        raise ValueError(
            "For four players, swissPairings should return two pairs.")
    # [(pid1, pname1, pid2, pname2), (pid3, pname3, pid4, pname4)] = pairings
    correct_pairs = set([frozenset([id1, id3]), frozenset([id2, id4])])
    actual_pairs = set([frozenset([pairings[0][0], pairings[0][2]]), frozenset([pairings[1][0], pairings[1][2]])])
    if correct_pairs != actual_pairs:
        raise ValueError(
            "After one match, players with one win should be paired.")
    print "12. After one match, players with one win are paired."


def testRematch():
    deleteTournaments()
    deleteMatches()
    deletePlayers()
    registerPlayer("Twilight Sparkle")
    registerPlayer("Fluttershy")
    registerTournament("Test Udacity Tournament")
    tournaments = getTournaments()
    tid = tournaments[0][0]
    standings = playerStandings()
    [id1, id2] = [row[0] for row in standings]
    reportMatch(id1, id2, tid, 'Test Report Match 1')
    try:
        # The database unique index should prevent this rematch
        reportMatch(id2, id1, tid, 'Test Report Match 2')
    except:
        print "13. Players weren't allowed to play a rematch."
        return

    raise ValueError(
            "Two players shouldn't be able to rematch.")


def testTournament():
    deleteTournaments()
    deleteMatches()
    deletePlayers()
    registerPlayer("Twilight Sparkle")
    registerPlayer("Fluttershy")
    registerPlayer("Applejack")
    registerPlayer("Pinkie Pie")
    registerTournament("Test Udacity Tournament")
    registerTournament("Test Nanodegree Tournament")
    tournaments = getTournaments()
    [tid1, tid2] = [row[0] for row in tournaments]
    standings = playerStandings()
    [id1, id2, id3, id4] = [row[0] for row in standings]
    reportMatch(id1, id2, tid1, 'Test Tournament 1-1')
    reportMatch(id3, id4, tid1, 'Test Tournament 1-2')
    reportMatch(id1, id2, tid2, 'Test Tournament 2-1')
    reportMatch(id3, id4, tid2, 'Test Tournament 2-2')
    standings = playerStandingsInTournament(tid1)
    if len(standings) != 4:
        raise ValueError(
            "There should be a total of four standings in the first tournament.")
    standings = playerStandingsInTournament(tid2)
    if len(standings) != 4:
        raise ValueError(
            "There should be a total of four standings in the second tournament.")
    
    print "14. After creating two pairs of matches as part of two different tournaments, no errors raised."


if __name__ == '__main__':
    testDeleteTournaments()
    testDeleteMatches()
    testDelete()
    testCount()
    testTournamentCount()
    testRegister()
    testRegisterTournament()
    testRegisterCountDelete()
    testRegisterCountDeleteTournaments()
    testStandingsBeforeMatches()
    testStandingsBeforeMatchesWithTournament()
    testReportMatches()
    testPairings()
    testRematch()
    testTournament()
    print "Success!  All tests pass!"


