import pymongo
from pymongo import MongoClient

connection = 'mongodb+srv://admin:<password>@cluster0.rthfj.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
cluster = MongoClient(connection)
db = cluster["test"]


print(cluster)