import pymongo
from pymongo import MongoClient
import environ  # for .env


env = environ.Env()
# reading .env file
environ.Env.read_env()

username = env('username')
password = env('password')

connection = 'mongodb+srv://{}:{}@cluster0.rthfj.mongodb.net/test?retryWrites=true&w=majority'.format(username, password)
cluster = MongoClient(connection)
db = cluster["test"]
collection = db['test']

post = {
    "_id": 1,
    "name": "Jim",
    "score": 8
}

collection.insert_one(post)
