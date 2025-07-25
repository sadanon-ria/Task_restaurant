from fastapi import APIRouter
from services.services import responseDefault, responseKeyword, responsePhoto
from datetime import datetime

from db.db import db, collection_name
from schemas.schemas import data_serializer

data = APIRouter()

@data.get("/allData", tags=["check all data"])
async def get_all():
    cursor = collection_name.find()
    data = list(cursor)
    return data_serializer(data)

@data.get("/dataDefault", tags=["Default บางซื่อ"])
async def get_default():
    return responseDefault()

@data.get("/dataKey/{keyword}", tags=["keyword"])
async def get_keyword(keyword:str):
    return responseKeyword(keyword)

@data.get("/dataPhoto/{fsq_place_id}", tags=["photo"])
async def get_photo(fsq_place_id:str):
    return responsePhoto(fsq_place_id)


# @data.post("/test-insert")
# async def insert_sample():
#     sample_data = {
#         "keyword": "บางซื่อ",
#         "results": [
#         {
#             "fsq_place_id": "4d2ecd026fc6f04d845f8445",
#             "name": "ลาบอุดรโภชนา",
#             "formatted_address": "1089 Krungthep-Nonthaburi 39, บางซื่อ, กรุงเทพมหานคร 10800",
#             "tel": "02 910 8177"
#         },
#         {
#             "fsq_place_id": "4c2ad9638abca593db5aff1f",
#             "name": "ก๋วยเตี๋ยวเรือ ลุงชลอ",
#             "formatted_address": "Khaema Market, บางซื่อ, กรุงเทพมหานคร 10800",
#             "tel": "02 911 8402"
#         }
#         ],
#         "timestamp": datetime.utcnow()
#     }
#     result = collection_name.insert_one(sample_data)
#     return {"inserted_id": str(result.inserted_id)}