from pymongo import MongoClient
import os

host = os.getenv("MONGO_HOST")
port = int(os.getenv("MONGO_PORT"))
username = os.getenv("MONGO_USERNAME")
password = os.getenv("MONGO_PASSWORD")
db_name = os.getenv("MONGO_DB")
auth_source = os.getenv("MONGO_AUTH_SOURCE")


def get_col():
    client = MongoClient(
        host=host,
        port=port,
        username=username,
        password=password,
    )
    db = client[db_name]
    return db['employees']
