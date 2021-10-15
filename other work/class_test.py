import mysql.connector

mydb =mysql.connector.connect(
user='root',
passwd ='pacoscout',
database='employeedb',
host='127.0.0.1',
allow_local_infile='1'
)

print(mydb)
myc=mydb.cursor()



myc.execute("drop database if exists employeedb ;")
myc.execute("create database employeedb;")
myc.execute("use employeedb")

myc.execute("drop table if exists Manages ;")
myc.execute("drop table if exists Employee ;")
myc.execute("drop table if exists Department ;")

myc.execute("""create table Employee (
  eid int,
  ename varchar(20),
  age int,
  salary float,
  residenceState char(2),
  dateHired date,
  Primary Key (eid) ) ;""")


myc.execute("""create table Department (
  did int,
  dname varchar(20),
  budget float,
  state char(2),
  city varchar(20),
  PRIMARY KEY (did) ) ;""")

myc.execute("""create table Manages (
  eid int,
  did int,
  departmentBudget int,
  dateStartedManaging date,
  PRIMARY KEY (did,eid));""")


myc.execute("insert into Employee values(1,'Sally1',55,24588,'CO','2017-10-7');")
myc.execute("insert into Employee values(2,'Sally2',24,44434,'CT','2017-11-21');")
myc.execute("insert into Employee values(3,'Sally3',39,58473,'DE','2017-4-3');")
myc.execute("insert into Employee values(4,'Sally4',54,45592,'AZ','2017-1-6');")
myc.execute("insert into Employee values(5,'Sally5',46,20332,'AL','2017-12-19');")
myc.execute("insert into Employee values(6,'Sally6',39,28111,'AL','2017-10-19');")
myc.execute("insert into Employee values(7,'Sally7',33,27332,'CO','2017-6-4');")
myc.execute("insert into Employee values(8,'Sally8',61,40111,'WI','2017-5-15');")

#count=myc.execute("select count(*) from employee;")
#print(count)

myc.execute("insert into Department values(101,'department1',5794,'CO', 'Denver');")
myc.execute("insert into Department values(102,'department2',7085,'CO', 'Lakewood');")
myc.execute("insert into Department values(103,'department3',null,'AZ', 'Pheonix');")
myc.execute("insert into Department values(104,'department4',9902,'AZ', 'Hotland');")
myc.execute("insert into Department values(105,'department5',9999,'NY', 'New york');")

#count=myc.execute("select count(*) from department;")
#print(count)
myc.execute("insert into Manages values(1, 101,5794,'2017-10-7');")
myc.execute("insert into Manages values(4, 103,5794,'2017-1-6');")
myc.execute("insert into Manages values(6,102,5794,'2017-10-19');")
myc.execute("insert into Manages values(5,105,5794,'2017-12-19');")

#count=myc.execute("select count(*) from manages;")
#print(count)


select p.* from players p where p.teamID=11
