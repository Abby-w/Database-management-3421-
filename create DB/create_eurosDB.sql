
drop database if exists Euros ;
create database Euros ;

show databases ;

use Euros ;

Drop table if exists Games;
Drop table if exists Players;
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
	index(year),
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

load data local infile '/Users/abbyward/Documents/DU coursework/databases 3421/data_stadiums.txt' into table stadiums
  fields terminated by ','
  lines terminated by '\n'
  ;
load data local infile '/Users/abbyward/Documents/DU coursework/databases 3421/data_teams.txt' into table teams
	fields terminated by ','
	lines terminated by '\n'
	;
load data local infile '/Users/abbyward/Documents/DU coursework/databases 3421/data_players.txt' into table players
  fields terminated by ','
  lines terminated by '\n'
  ;
SET FOREIGN_KEY_CHECKS = 0;
load data local infile '/Users/abbyward/Documents/DU coursework/databases 3421/data_games.txt' into table games
	fields terminated by ','
	lines terminated by '\n'
	;
