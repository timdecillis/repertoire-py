from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017") #might need /fetcher?
db = client['mind_palace']
collection = db['users']
# need to connect to db?