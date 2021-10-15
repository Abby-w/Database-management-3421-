drop database if exists Sailing ;
create database Sailing ;

show databases ;

use Sailing ;

drop table if exists Sailors ;

create table Sailors (
  sid int,
  name varchar(20) NOT NULL,
  age int,
  rating float NOT NULL,
  Primary Key (sid) ) ;

insert into Sailors values (1, "Mary", 24, 5);
insert into Sailors values (2, "John", 22, 3);


drop table if exists Reserve ;

create table Reserve (
  sid int,
  bid int,
  rdate date) ;

insert into Reserve values (1, 101, '2001-01-01');
insert into Reserve values (2, 101, '1999-12-31');
insert into Reserve values (1, 102, '2000-01-01');

describe Sailors;

select * from Sailors ;

select * from Reserve ;

select * from Sailors S, Reserve R where S.sid=R.sid ;
