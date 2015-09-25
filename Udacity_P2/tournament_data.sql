-- Udacity Nanodegree: Fullstack Web Developer
-- File: tournament_data.sql -- Test Insertions
-- Author: Fernando Matarrubia

-- Some test insertions here, so we can avoid doing everything manually
INSERT INTO players(name) VALUES ('Michael Jordan'); 	-- id: 1
INSERT INTO players(name) VALUES ('Shaquille ONeal'); 	-- id: 2
INSERT INTO players(name) VALUES ('Carmelo Anthony'); 	-- id: 3
INSERT INTO players(name) VALUES ('Stephen Curry');		-- id: 4
INSERT INTO players(name) VALUES ('Kevin Durant');		-- id: 5
INSERT INTO players(name) VALUES ('Pau Gasol');			-- id: 6

INSERT INTO tournaments(name) VALUES ('NPPA Season 2014/2015');

INSERT INTO matches VALUES (1, 1, 2, 'Bulls vs Lakers');
INSERT INTO matches VALUES (1, 3, 4, 'Knicks vs Warriors');
INSERT INTO matches VALUES (1, 4, 2, 'Warriors vs Lakers');
INSERT INTO matches VALUES (2, 4, 2, 'Warriors vs Knicks');


