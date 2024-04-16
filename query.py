import pymongo

myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017")


print(myclient)

mydb = myclient["persons"]
mycoll = mydb["customers"]


myquery = {"name": "Alan"}

mydoc = mycoll.find(myquery)

for x in mydoc:
    print(x["address"])