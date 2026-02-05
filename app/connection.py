from pymongo import MongoClient
import os

host = os.getenv("MONGO_HOST")
port = int(os.getenv("MONGO_PORT"))



def get_col():
    client = MongoClient(
        host=host,
        port=port
    )
    db = client["week_16"]
    return db['employees']
