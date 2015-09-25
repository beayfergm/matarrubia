-- Udacity Nanodegree: Fullstack Web Developer
-- File: tournament.sql -- SQL Table definitions for the tournament project and some test insertions
-- Author: Fernando Matarrubia

-- Dropping the database and showing a notice if it already exists
DROP DATABASE IF EXISTS tournament;

-- Creating the database 
CREATE DATABASE tournament;

-- Connecting to the database
\c tournament

-- Creating all the tables
CREATE TABLE players ( id SERIAL PRIMARY KEY, 
					   	name TEXT );


CREATE TABLE tournaments ( id SERIAL PRIMARY KEY, 
						   name TEXT ); 


-- (ON DELETE CASCADE) Reference: http://www.postgresql.org/docs/8.2/static/ddl-constraints.html
CREATE TABLE matches ( tournament_id INT references tournaments(id) ON DELETE CASCADE,
					   winner_id INT references players(id) ON DELETE CASCADE,
					   loser_id INT references  players(id) ON DELETE CASCADE CHECK (loser_id <> winner_id),
					   comments TEXT );


-- Creating a Unique Index
-- This index prevents two players to play agains each other twice in the same tournament
-- Reference: http://stackoverflow.com/questions/25647360/constraint-to-avoid-combination-of-foreign-keys
CREATE UNIQUE INDEX matches_rematch_idx
   ON matches (tournament_id, least(winner_id, loser_id), greatest(winner_id, loser_id));


-- Creating a view to make easier showing the Player Standings
-- Reference (for conditional counting: http://stackoverflow.com/questions/21288458/in-redshift-postgres-how-to-count-rows-that-meet-a-condition)
CREATE VIEW playerStandings AS 
	SELECT 
		players.id, players.name, matches.tournament_id, COUNT(CASE WHEN players.id = matches.winner_id THEN 1 END) as wins, COUNT(CASE WHEN matches.tournament_id IS NOT NULL THEN 1 END) as matches
	FROM 
		players left join matches
	ON 
		players.id = matches.winner_id OR players.id = matches.loser_id
	GROUP BY players.id, matches.tournament_id
	ORDER BY wins DESC;

-- We need to insert this test tournament to the original test suite completes successfully
INSERT INTO tournaments(name) VALUES ('Test Udacity Tournament');	-- id: 1


