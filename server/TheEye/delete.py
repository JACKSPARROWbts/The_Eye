
from pymongo import MongoClient
l=[]
truevalues=[]
try:
	conn = MongoClient()
	print("Connected successfully!!!")
except:
	print("Could not connect to MongoDB")

db = conn.TheEye

collection = db.InfoDB_lead

emp_rec1 = {
		"name":"thats it",
		}

cursor = collection.find()
for record in cursor:
	l.append(record["name"])
for i in range(len(l)):
	truevalues.append(l[i]==emp_rec1["name"])
if True in truevalues:
	print("True")
else:
	rec_id1=collection.insert_one(emp_rec1)
	print(rec_id1)
