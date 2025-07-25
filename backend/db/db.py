from pymongo import MongoClient
from decouple import config

username = config("dbUser")
password = config("dbPass")

# print(username)
# print(password)
url = f"mongodb+srv://{username}:{password}@cluster0.hjtxlfu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# print(url)
Client = MongoClient(url)
db = Client.cacheKeyword

collection_name = db["cacheKeyword"]