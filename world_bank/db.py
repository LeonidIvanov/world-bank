from pymongo import MongoClient

client = MongoClient('localhost', 27017)
mongo_db = client.world_bank
