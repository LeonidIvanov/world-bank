from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient('localhost', 27017)
mongo_db = client.world_bank
