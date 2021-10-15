import mysql.connector

mydb =mysql.connector.connect(
user='root',
passwd ='pacoscout',
database='euros',
host='127.0.0.1',
allow_local_infile='1'
)

print(mydb)
myc=mydb.cursor(buffered=True)
myc2=mydb.cursor(buffered=True)

myc.execute("use Euros")


##Assume all the players from one regular season teeam are disqalified and need to be deleted from the current year's country teams
##Then return the list of players on each team to know how many players they need to add to their roster
print("Regular teams:")
myc.execute("select distinct regularTeam from Players")
row=myc.fetchone()
while row is not None:
    print(row)
    row=myc.fetchone()

inputTeam=input("Please enter the team which is disqualified: ")
inputYear=int(input("Please enter the current year: "))

print("Positions for each country that can be filled")
command1 =f"""select p.position, t.countryName from players p, teams t where p.regularTeam='{str(inputTeam)}' and t.teamID=p.teamID and t.year={str(inputYear)}"""
myc.execute(command1)
row=myc.fetchone()
replace=[]
while row is not None:
    replace+=[(row)]
    print(row)
    row=myc.fetchone()


command2 =f"""select p.* from players p, teams t where p.regularTeam='{str(inputTeam)}' and t.teamID=p.teamID and t.year={str(inputYear)}"""
myc.execute(command2)
value=0
for row in myc:
    print(row)
    ID=row[0]
    print(ID)
    command3=f"delete from players where playerID={ID};"
    print(command3)
    #not actually deleting for some reason
    try:

        myc2.execute(command3)
        mydb.commit()
    except:
        mydb.rollback()
    newplayer=input(f"Do you want to add a new player for {replace[value][1]} for the position of {replace[value][0]}(Yes or No)")
    if newplayer.lower()=="yes":
        name=input("Please enter player name:")
        age=input("please enter age:")
        regularTeam=input("Please enter regular team name (from list above):")
        command5=f"""select teamID from teams where year={inputYear} and countryName='{str(replace[value][1])}';"""
        print(command5)
        myc2.execute(command5)
        team=myc2.fetchone()
        command4=f"""insert into players values({row[0]}, '{name}', {team[0]}, '{row[3]}', {age},0,0,0,'{regularTeam}');"""
        print(command4)
        myc2.execute(command4)
        mydb.commit()
    else:
        print(f"{replace[value][0]} will not be added to {replace[value][1]}")
    value+=1
    
