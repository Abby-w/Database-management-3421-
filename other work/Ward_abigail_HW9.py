import pymongo
import pprint
from pymongo import MongoClient

client = MongoClient()# connects default host


db = client.db_people


#Q1
for object in db.thePeople.find({'numChildren':7}):
    pprint.pprint(object)

#Q2
for object in db.thePeople.find({'numChildren':7}, {'_id':0, 'pid':1, 'state':1, 'children':1}):
    pprint.pprint(object)

#Q3
for object in db.thePeople.find({'numChildren':6, 'state':'CA'}):
    pprint.pprint(object)

#Q4
for object in db.thePeople.find({'numChildren':{"$in":[6,7]}, 'state':'CA'}):
    pprint.pprint(object)

#Q5
for object in db.thePeople.find({'children':{'$regex':'Bob A'}}, {'_id':0, 'pid':1, 'children':1}):
    pprint.pprint(object)

#Q6
for object in db.thePeople.aggregate([{'$group':{'_id':'$numChildren', 'numFamilies': {'$sum':1}}}]):
    pprint.pprint(object)

#Q7
for object in db.thePeople.aggregate([ {'$group':{'_id':'$state', 'avgSalary': {'$avg':'$salary'}, 'numInGroup': {'$sum':1}}}, {'$sort':{'_id':1}}]):
    pprint.pprint(object)

#Q8
for object in db.thePeople.aggregate([{'$match':{'state':'WI'}}, {'$group':{'_id':'$state', 'avgSalary': {'$avg':'$salary'}, 'numInGroup': {'$sum':1}}}]):
    pprint.pprint(object)

#Q9
for object in db.thePeople.aggregate([{'$match':{'state':{"$in":["ND","SD","NE", "KS","MN", "IA" , "MS", "WI", "IL", "IN", "MI", "OH"]}}}, {'$group':{'_id':'$state', 'avgSalary': {'$avg':'$salary'}, 'minSalary': {'$min':'$salary'}, 'maxSalary': {'$max':'$salary'}, 'numInGroup': {'$sum':1}}}, {'$sort':{'_id':1}}]):
    pprint.pprint(object)

#Q10
for object in db.thePeople.aggregate([ {'$group':{'_id':'$state', 'avgSalary': {'$avg':'$salary'}, 'numInGroup': {'$sum':1}}},{'$match':{'avgSalary':{'$gte':82000}}},  {'$sort':{'_id':1}}]):
    pprint.pprint(object)

#Q11
for object in db.thePeople.aggregate([{'$match':{'state':{"$in":["ND","SD","NE", "KS","MN", "IA" , "MS", "WI", "IL", "IN", "MI", "OH"]}}},  {'$group':{'_id':'$state', 'avgSalary': {'$avg':'$salary'}, 'minSalary': {'$min':'$salary'}, 'maxSalary': {'$max':'$salary'},'numInGroup': {'$sum':1}}},{'$match':{'avgSalary':{'$gte':82000}}},  {'$sort':{'_id':1}}]):
    pprint.pprint(object)


#update one

for object in db.thePeople.find({'firstName':'Bob'}):
    pprint.pprint(object)
    break

for object in db.thePeople.aggregate([ {'$match':{'firstName':'Bob'}}, {'$group':{'_id':'$firstName', 'numInGroup': {'$sum':1}}}]):
    pprint.pprint(object)


aQuery = {'firstName':{'$regex':'Bob'}}
aChange = {'$set':{'firstName':'Robert'}}
db.thePeople.update_one(aQuery, aChange)

for object in db.thePeople.aggregate([ {'$match':{'firstName':'Bob'}}, {'$group':{'_id':'$firstName', 'numInGroup': {'$sum':1}}}]):
    pprint.pprint(object)

for object in db.thePeople.find({'firstName':'Robert'}):
    pprint.pprint(object)



#update many

for object in db.thePeople.find({'firstName':'Joseph'}):
    pprint.pprint(object)

for object in db.thePeople.aggregate([ {'$match':{'firstName':'Joseph'}}, {'$group':{'_id':'$firstName', 'numInGroup': {'$sum':1}}}]):
    pprint.pprint(object)


aQuery = {'firstName':'Joseph'}
aChange = {'$set':{'firstName':'Joe'}}
db.thePeople.update_many(aQuery, aChange)

for object in db.thePeople.aggregate([ {'$match':{'firstName':'Joseph'}}, {'$group':{'_id':'$firstName', 'numInGroup': {'$sum':1}}}]):
    pprint.pprint(object)



#delete many

for object in db.thePeople.find({'firstName':'Bob'})[:5]:
    pprint.pprint(object)

for object in db.thePeople.aggregate([ {'$match':{'firstName':'Bob'}}, {'$group':{'_id':'$firstName', 'numInGroup': {'$sum':1}}}]):
    pprint.pprint(object)

db.thePeople.delete_many({'firstName':'Bob', 'MI':'C'})

for object in db.thePeople.find({'firstName':'Bob'})[:5]:
    pprint.pprint(object)

for object in db.thePeople.aggregate([ {'$match':{'firstName':'Bob'}}, {'$group':{'_id':'$firstName', 'numInGroup': {'$sum':1}}}]):
    pprint.pprint(object)
