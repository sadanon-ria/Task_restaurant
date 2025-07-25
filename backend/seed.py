from pymongo import MongoClient
from datetime import datetime
from decouple import config

username = config("dbUser")
password = config("dbPass")

url = f"mongodb+srv://{username}:{password}@cluster0.hjtxlfu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
Client = MongoClient(url)
db = Client.cacheKeyword

collection_name = db["cacheKeyword"]

data = {
    "keyword": "บางซื่อ",
    "results": [
        {
            "fsq_place_id": "4d2ecd026fc6f04d845f8445",
            "name": "ลาบอุดรโภชนา",
            "formatted_address": "1089 Krungthep-Nonthaburi 39, บางซื่อ, กรุงเทพมหานคร 10800",
            "tel": "02 910 8177"
        },
        {
            "fsq_place_id": "4c2ad9638abca593db5aff1f",
            "name": "ก๋วยเตี๋ยวเรือ ลุงชลอ",
            "formatted_address": "Khaema Market, บางซื่อ, กรุงเทพมหานคร 10800",
            "tel": "02 911 8402"
        }
    ],
    "timestamp": datetime.utcnow()
}

result = collection_name.insert_one(data)
print(f"Inserted ID: {result.inserted_id}")
