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


-- Some test insertions here, so we can avoid doing everything manually
INSERT INTO players(name) VALUES ('Michael Jordan'); 	-- id: 1
INSERT INTO players(name) VALUES ('Shaquille ONeal'); 	-- id: 2
INSERT INTO players(name) VALUES ('Carmelo Anthony'); 	-- id: 3
INSERT INTO players(name) VALUES ('Stephen Curry');		-- id: 4

INSERT INTO tournaments(name) VALUES ('NPPA Season 2014/2015'); 	-- id: 1
INSERT INTO tournaments(name) VALUES ('NPPA Season 2015/2016'); 	-- id: 2

INSERT INTO matches VALUES (1, 1, 2, 'Bulls vs Lakers');
INSERT INTO matches VALUES (1, 3, 4, 'Knicks vs Warriors');
INSERT INTO matches VALUES (1, 4, 2, 'Warriors vs Lakers');
INSERT INTO matches VALUES (2, 4, 2, 'Warriors vs Knicks');


