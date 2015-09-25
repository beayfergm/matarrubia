# Project 2: Tournament Results 

![Udacity Logo](https://lh5.ggpht.com/2Khq0jHkIOhW2VKiGOcJ97rTslkGqu0fDoI-bqrvugAoop9eAFvA_wmneVDcGpaTFDEQCja7dTRQTnHZiA=s0)

This folder contains materials related with my second Udacity Full Stack Web Developer Nanodegree Project

### Dependencies:

This project uses [PostgreSQL](http://www.postgresql.org/) and [Python](https://www.python.org/). It has been developed using a preconfigured virtual machine (using [Vagrant](https://www.vagrantup.com/) and [Virtualbox](https://www.virtualbox.org/)).
All the installation instructions for this setup can be found in this GitHub repo: [udacity/fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm).

### How to run the application

This instructions assume that the user already has a configured VM, and is able to access the project files from inside the VM. 

1.- Checkout this repository: [beayfergm/matarrubia](https://github.com/beayfergm/matarrubia)

2.- Copy the following files into a folder of your choosing (this folder MUST be accesible from the VM):
```
Udacity_P2/tournament.py
Udacity_P2/tournament.sql
Udacity_P2/tournament_test.py
Udacity_P2/tournament_test_updated.py
```

3.- Open the terminal, initialize the VM and cd into your custom folder (/vagrant/tournament is the default for the previously mentioned preconfigured VM). This folder MUST contain the files copied in the previous step:
```
custom_path_to_vm_folder$ vagrant up && vagrant ssh
(...)
vagrant@vagrant-ubuntu-trusty-32:~$ cd /vagrant/tournament
```

4.- Start a psql terminal session (this should change the terminal prompt):

```
psql
```

5.- Execute the provided .sql file. This will create the database, connect to it, create all the tables, an index, and a custom view. After that, it will insert some test data. 
```
vagrant=> \i tournament.sql
```

6.- As a result of the previous command, you should see the following output (the first line won't show if you have executed this command before):
```
DROP DATABASE
CREATE DATABASE
You are now connected to database "tournament" as user "vagrant".
CREATE TABLE
CREATE TABLE
CREATE TABLE
CREATE INDEX
CREATE VIEW
INSERT 0 1
tournament=>
```

6.1.- (**Optional**) There is a separate .sql file which inserts some test data into the database. You can execute it if you want, using the following command. The presented output should appear:
```
tournament=> \i tournament_data.sql
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
INSERT 0 1
```

6.2.- (**Optional, after 6.1**) To doublecheck that everything just worked, execute the next command (still inside the psql terminal session). You should expect the following output:
```
tournament=> SELECT * FROM players;
 id |      name
----+-----------------
  1 | Michael Jordan
  2 | Shaquille ONeal
  3 | Carmelo Anthony
  4 | Stephen Curry
  5 | Kevin Durant
  6 | Pau Gasol
(6 rows)
```

7.- Finish the psql interactive terminal session using the following command:
```
tournament=> \q
```

8.- Execute the test suite:
```
python tournament_test.py

1. Old matches can be deleted.
2. Player records can be deleted.
3. After deleting, countPlayers() returns zero.
4. After registering a player, countPlayers() returns 1.
5. Players can be registered and deleted.
6. Newly registered players appear in the standings with no matches.
7. After a match, players have updated standings.
8. After one match, players with one win are paired.
Success!  All tests pass!
```

9.- (**Optional**) Execute the updated test suite:
```
python tournament_test_updated.py

0. Old tournaments can be deleted.
1. Old matches can be deleted.
2. Player records can be deleted.
3. After deleting, countPlayers() returns zero.
4. After deleting, countTournaments() returns zero.
5. After registering a player, countPlayers() returns 1.
6. After registering one tournament, countTournaments() returns 1.
7. Players can be registered and deleted.
8. Tournaments can be registered and deleted.
9. Newly registered players appear in the standings with no matches.
10. Newly registered players do not appear in an specific tournament standings with no matches.
11. After a match, players have updated standings.
12. After one match, players with one win are paired.
13. Players weren't allowed to play a rematch.
14. After creating two pairs of matches as part of two different tournaments, no errors raised.
Success!  All tests pass!
```


 Enjoy!

