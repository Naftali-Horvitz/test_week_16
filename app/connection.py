from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client['week_16']

def get_col():
    return db['employees']
