import requests
from decouple import config
from db.db import collection_name
from schemas.schemas import data_serializer
from datetime import datetime, timedelta

# สำหรับดึงข้อมูลรูป
def responsePhoto(fsq_place_id:str):
    url = "https://places-api.foursquare.com/places/" + fsq_place_id +"/photos"
    headers = {
        "accept": "application/json",
        "X-Places-Api-Version": "2025-06-17",
        "authorization": config("authorization")
    }
    # response = requests.get(url, headers=headers).json()
    # return response
    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        if response.status_code == 429 or "Your account has no API credits remaining" in data.get("message", ""):
            return None  
        return data
    except Exception as e:
        print(f"Error fetching photo: {e}")
        return None
    

# *****************************แบบแรก******************************************
# def responseDefault():
#     default = "บางซื่อ"
#     URL = config("url") + "?query=ร้านอาหาร&near=" + default + "&limit=2"
#     headers = {
#         "accept": config("accept"),
#         "X-Places-Api-Version": config("X-Places-Api-Version"),
#         "authorization": config("authorization")
#     }
#     dataRes = requests.get(URL, headers=headers).json()
#     return dataRes
# *****************************แบบสอง******************************************
def responseDefault():
    default = "บางซื่อ"
    return responseKeyword(default)
# *****************************************************************************


# ใช้ตอนหาใน database แล้วไม่เจอ key word
def dataApi(keyword:str):
    URL = config("url") + "?query=ร้านอาหาร&near="+keyword+"&limit=10"
    headers = {
        "accept": config("accept"),
        "X-Places-Api-Version": config("X-Places-Api-Version"),
        "authorization": config("authorization")
    }
    dataKey = requests.get(URL, headers=headers).json()
    results = []
    for place in dataKey.get("results", []):
        fsq_id = place.get("fsq_place_id")
        name = place.get("name")
        formatted_address = place.get("location", {}).get("formatted_address")
        tel = place.get("tel")

        results.append({
            "fsq_place_id": fsq_id,
            "name": name,
            "formatted_address": formatted_address,
            "tel": tel
        })

    template = {
        "keyword": keyword,
        "results": results,
        "timestamp": datetime.utcnow()
    }
    inserted  = collection_name.insert_one(template)
    resultsKey = data_serializer(collection_name.find_one({"_id": inserted.inserted_id}))
    return resultsKey

def responseKeyword(keyword:str):
# เขียน if ถ้ามี keyword ใน db ให้ get มาแสดงผล ถ้าไม่มีให้ใช้ api แล้วแสดงผล + เก็บลง db ใหม่
    # dataKey = collection_name.find_one({"keyword":keyword})
    # print(dataKey)
    for data in collection_name.find():
        if data.get("keyword") == keyword:
            # เช็คก่อนว่า data เก่าหรือยัง
            timestamp = data.get("timestamp")
            if timestamp:
                expire_time = timedelta(hours=1)
                if datetime.utcnow() - timestamp < expire_time:
                    result = data_serializer(collection_name.find_one({"keyword":keyword}))
                    return result
                
            collection_name.delete_one({"_id": data["_id"]})
    return dataApi(keyword)



# print(responseKeyword("data2"))
# print(responseKeyword("สยาม"))


# dataKey = collection_name.find_one({"keyword":"not in data"})
# print(dataKey)
# dataKeytest = collection_name.find_one({"keyword":"example keyword"})
# print(dataKeytest)



# for data in collection_name.find():
#     if data.get("keyword") == "not in data":
#         print (False)
#     elif data.get("keyword") == "example keyword":
#         print (True)