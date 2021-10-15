import pymongo
import pprint
from pymongo import MongoClient

client = MongoClient()# connects default host


db = client.performances2
group=db.group
venues=db.venues
upcomingPerformances=db.upcomingPerformances

bands=[{'name':'band1','numberMembers':5, 'costToBook':4000, 'genre':'rock'},
{'name':'band2','numberMembers':2, 'costToBook':900, 'genre':'pop'} ,
 {'name':'band3','numberMembers':8, 'costToBook':1200, 'genre':'jazz'},
 {'name':'band4','numberMembers':4, 'costToBook':1000000, 'genre':'rap'},
{'name':'band5','numberMembers':2, 'costToBook':10000, 'genre':'r&b'}]

#group.insert_many(bands)

places=[{'name':'red rocks', 'city':'Denver', 'seatingCapacity':20000},
{'name':'Madison Square Garden', 'city':'New York', 'seatingCapacity':50000},
{'name':'United Center', 'city':'Chicago', 'seatingCapacity':20000}]
#venues.insert_many(places)

event={'groupName':'band1','venueDate':['red rocks', '2021-08-12']}
#upcomingPerformances.insert_one(event)

#for object in group.find():
#    pprint.pprint(object)

#for obj in db.group.find({'genre':{'$regex':'roc'}}):
#    pprint.pprint(obj)

#group.delete_one({'name':'band1'})

#for object in group.find():
#    pprint.pprint(object)

delete_bands=[{'name':'band2'},{'name':'band3'}]
group.delete_many(delete_bands)

for object in group.find():
    pprint.pprint(object)
