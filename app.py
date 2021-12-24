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

# with id
post = {
    "_id": 1,
    "name": "Wim",
    "score": 19
}
# collection.insert_one(post)

# without id, and it will auto generated
post = {
    "name": "Mark",
    "score": 3
}
# collection.insert_one(post)

# multiple insert
post1 = {"name": "Sam"}
post2 = {"name": "Luna"}
# collection.insert_many([post1, post2])

# get all
results = collection.find()  # more expressions https://pymongo.readthedocs.io/en/stable/tutorial.html#

print('find: get all')
for r in results:
    print(r)
    print(r['_id'])

# get by certain name
results = collection.find({"name": "Mark"})


print('-----------\nfind')
# for r in results:
#     print(r)
#     print(r['_id'])

result = collection.find_one({"_id": 1})

print('-----------\nfind_one:', result)

# delete one
print('\ndelete:')
# collection.delete_one({"_id": 1})


# delete many
# collection.delete_many({"name": "Sam"})

# delete all
print('\ndelete all:')
collection.delete_many({})
