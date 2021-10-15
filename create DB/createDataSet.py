import pandas as pd
import numpy as np
import random,requests
from bs4 import BeautifulSoup as BS
from faker import Faker
import csv
import datetime
#initialize Faker
fake=Faker()



##Stadiums

wiki = requests.get('https://en.wikipedia.org/wiki/List_of_European_stadiums_by_capacity')
soup = BS(wiki.content, 'html.parser')

tables=soup.find_all('table', class_="wikitable")[:7]
# extract the column names
column_names = [item.get_text() for item in tables[0].find_all('th')][1:8]
columnNames = [s.replace("\n", "") for s in column_names]

# extract the content
contents = [item.get_text() for item in tables[0].find_all('td')]

values=[]
for table in tables:
    for item in table.select('td'):
        temp = item.get_text()
        values.append(temp.strip())

data = np.reshape(values,(307,7))
# put all the data into a dataframe
df = pd.DataFrame(data = data, columns=columnNames)


snames=df["Name"].values.tolist()
location=df["City"].values.tolist()
numberOfSeats=[]
for n in range(0,307):
    numberOfSeats.append(random.randint(17000, 150000))

dict = {"sname": snames, "location":location, "numberOfSeats":numberOfSeats}

df = pd.DataFrame(dict)

df.to_csv(index=False, path_or_buf='stadiums.txt', header=False, line_terminator='\n')


with open('stadiums.txt', 'r') as f, open('data_stadiums.txt', 'w') as fo:
    for line in f:
        fo.write(line.replace('"', '').replace("'", ""))

#teams
Countries=["Russia","Germany","United Kingdom", "France", "Italy", "Spain" , "Ukraine", "Poland",
"Romania", "Netherlands", "Belgium" , "Czech Republic", "Greece", "Portugal", "Sweden", "Hungary",
"Belarus", "Austria", "Serbia", "Switzerland", "Bulgaria", "Denmark", "Finland", "Slovakia", "Norway",
"Ireland", "Croatia", "Moldova", "Bosnia", "Albania" , "Lithuania", "North Macedonia", "Slovenia",
"Latvia", "Estonia", "Montenegro", "Luxembourg", "Malta", "Iceland", "Andorra", "Monaco", "Liechtenstein"]



countryName=[]
year=[]
wins=[]
losses=[]
ties=[]

IDs=range(1, 8881)
n_teams=40
for y in range(1800,2022):
    countryName+=random.sample((Countries),40)

    for n in range(0,n_teams):
        wins.append(random.randint(0, 7))
        losses.append(random.randint(0,3))
        ties.append(random.randint(0, 3))
        year.append(y)



dict = {"teamID":IDs,"countryName": countryName, "year":year, "wins": wins, "losses": losses, "ties":ties}
df = pd.DataFrame(dict)
df.to_csv(index=False, path_or_buf='data_teams.txt', header=False)


#Players

names=[]
teamID=[]
position=[]
age=[]
goals=[]
assists=[]
yellowCards=[]
regularTeam=[]

positions=["goalie",
"defender","defender","defender","defender",
"midfielder","midfielder","midfielder","midfielder",
"forward", "forward", "goalie",
"defender","defender","defender","defender",
"midfielder","midfielder","midfielder","midfielder",
"forward", "forward", "goalie",
"defender","defender","defender","defender",
"midfielder","midfielder","midfielder","midfielder",
"forward", "forward"]

regularTeams=["Bayern Munich", "Sevilla", "Real Madrid", "Barcelona", "Atletico Madrid", "Liverpool", "Manchester City", "Manchester United", "Chelsea", "Juventus", "Inter Milan",
"Atalanta", "Lazio", "Borussia Dortmund", "RB Leipzig", "Borussia Monchengladbach", "PSG", "Marseille", "Rennes", "Zenit", "Lokomotiv Moscow", "Krasnodar", "Porto", "Club Brugge"
, "Shakhtar Donetsk", "Dynamo Kiev", "Istanbul Basaksehir", "Ajax", "Red Bull Salzburg", "Olympiacos", "Midtyjlland", "Ferencvaros"]


IDs=range(1, 293041)
for team in range(1,8881):
    for p in positions:
        teamID.append(team)
        names.append(fake.name())
        position.append(p)
        age.append(random.randint(17, 40))
        if p=="goalie":
            goals.append(0)
        else:
            goals.append(random.randint(0, 4))
        assists.append(random.randint(0,2))
        yellowCards.append(random.randint(0, 2))
        regularTeam.append(random.choice(regularTeams))



dict = {"playerID": IDs, "name": names, "teamID":teamID, "position": position, "Age": age, "goals": goals, "assists":assists,
"yellowCards":yellowCards, "regularTeam":regularTeam}

df = pd.DataFrame(dict)

df.to_csv(index=False, path_or_buf='data_players.txt', header=False)


#games
gameID=[]
gameNumber=[]
sname=[]
team1=[]
team2=[]
roundName=[]
gdate=[]
team1score=[]
team2score=[]



rounds=["Group A", "Group A","Group A","Group A","Group A","Group A",
"Group B","Group B","Group B","Group B","Group B","Group B",
"Group C","Group C","Group C","Group C","Group C","Group C",
"Group D","Group D", "Group D", "Group D","Group D", "Group D",
 "Group E",  "Group E",  "Group E",  "Group E","Group E",  "Group E",
 "Group F", "Group F", "Group F", "Group F","Group F", "Group F",
  "Round of 16", "Round of 16",  "Round of 16",  "Round of 16",
  "Round of 16",  "Round of 16",  "Round of 16",  "Round of 16",
   "Quaterfinals",  "Quaterfinals", "Quaterfinals", "Quaterfinals",
   "Semifinals",  "Semifinals", "Finals"]
IDs=range(1, 11323)
teamIDs=range(1, 8881)
years=range(1800,2022)
teamstart=0
teamend=24
for year in years:
    n=1
    start_date = datetime.date(year, 5, 1)
    end_date = datetime.date(year, 8, 1)
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days

    for r in rounds:
        gameNumber.append(n)
        n=n+1
        sname.append(random.choice(snames))
        teamone=random.choice(teamIDs[teamstart:teamend])
        teamtwo=random.choice(teamIDs[teamstart:teamend])
        while teamone==teamtwo:
            teamtwo=random.choice(teamIDs[teamstart:teamend])
        team1.append(teamone)
        team2.append(teamtwo)
        roundName.append(r)
        random_number_of_days = random.randrange(days_between_dates)
        gd=start_date + datetime.timedelta(days=random_number_of_days)
        gdate.append(gd)
        team1score.append(random.randint(0,5))
        team2score.append(random.randint(0,5))
    teamstart+=24
    teamend+=24

dict = {"gameID":IDs, "gameNumber": gameNumber, "sname":sname, "team1ID":team1,
"team2ID":team2, "roundName":roundName, "gdate":gdate, "team1score":team1score, "team2score":team2score }
df = pd.DataFrame(dict)
df.to_csv(index=False, path_or_buf='data_games.txt', header=False)
