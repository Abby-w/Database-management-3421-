/usr/local/mysql/bin/mysql --local-infile=1 -u root -p
load data local infile '/Users/abbyward/Downloads/data_reserve.txt' into table reserve   fields terminated by ','   lines terminated
by '\n';
source createAndLoadSailorDB.txt;
SHOW GLOBAL VARIABLES LIKE 'local_infile';
set global local_infile = 1;


load data local infile '/Users/abbyward/Documents/DU coursework/databases 3421/untitled folder/data_players.txt' into table players
  fields terminated by ','
  lines terminated by '\n'
  ;


load data local infile '/Users/abbyward/Documents/DU coursework/databases 3421/untitled folder/data_stadiums.txt' into table stadiums
  fields terminated by ','
  lines terminated by '\n'
  ;

load data local infile '/Users/abbyward/Documents/DU coursework/databases 3421/untitled folder/data_teams.txt' into table teams
	fields terminated by ','
	lines terminated by '\n'
	;

SET FOREIGN_KEY_CHECKS = 0;
load data local infile '/Users/abbyward/Documents/DU coursework/databases 3421/untitled folder/data_games.txt' into table games
	fields terminated by ','
	lines terminated by '\n'
	;
drop database if exists Euros ;
create database Euros ;

show databases ;

use Euros ;

Drop table if exists Players;
Drop table if exists Games;
Drop table if exists Teams;
Drop table if exists Stadiums;




Create table Stadiums (
	sname varchar(50) NOT NULL,
	location varchar(30) NOT NULL,
	numberrOfSeats int,
	Primary Key (sname));

Create table Teams (
	teamID int NOT NULL,
	countryName varchar(30) NOT NULL,
	year int,
	wins int,
	losses int,
	ties int,
	Primary Key (teamID));

Create table Games (
	gameID int NOT NULL,
	gameNumber int,
	sname varchar(60),
	team1ID int,
	team2ID int,
	roundName varchar(20),
	gdate date,
	team1score int,
	team2score int,
	Primary Key (gameID),
	FOREIGN KEY (team1ID) REFERENCES Teams(teamID),
	FOREIGN KEY (team2ID) REFERENCES Teams(teamID),
	FOREIGN KEY (sname) REFERENCES Stadiums(sname));


Create table Players (
	playerID int NOT NULL,
	name varchar(30) NOT NULL,
	teamID int NOT NULL,
	position varchar(20),
	age int,
	goals int,
	assists int,
	yellowCards int,
	regularTeam varchar(30),
	PRIMARY KEY (playerID),
  FOREIGN KEY (teamID) REFERENCES Teams(teamID) ) ;

insert into players values(63889, "Abby Ward", 3000, "defender", 23,4,0,0,"Red Bull Salzburg")

insert into Teams values ("Turkey", 0, 0, 0);
insert into Teams values ("Italy", 0,0,0);
insert into Teams values ("Wales", 0, 0, 0);
insert into Teams values ("Switzerland", 0,0,0);
insert into Games values (1, "Studio Olymico","Turkey", "Germany", "Group A", '2021-06-11', 0, 3);


  IF (inteam1score>inteam2score)
  SET winner  = (select t.countryName from teams t, games g where t.teamID=g.team1ID and g.gameID=ingameID)
  IF (inteam1score<inteam2score)
  SET winner  = (select t.countryName from teams t, games g where t.teamID=g.team2ID and g.gameID=ingameID)
  ELSE
  SET winner  = "tie"
  ;


IF (inteam1score > inteam2score) then
select t.countryName INTO outwinner
from teams t, games g
where t.teamID=g.team1ID and g.gameID=ingameID;

IF (inteam1score < inteam2score) then
select t.countryName INTO outwinner
from teams t, games g
where t.teamID=g.team2ID and g.gameID=ingameID;

IF (inteam1score = inteam2score) then
SET outwinner := "tie";

SELECT t.countryname
	CASE
            WHEN inteam1score> inteam2score
               THEN t.teamID=g.team1ID
               ELSE t.teamID=g.team2ID
       END into outwinner
FROM teams t, games g
where  and g.gameID=ingameID;
