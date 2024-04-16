import pymongo

myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017")


print(myclient)

mydb = myclient["persons"]
mycoll = mydb["customers"]


myreg = {"name": "Alan", "address": "los arcos 25"}

x = mycoll.insert_one(myreg)