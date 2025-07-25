Backend

Frameworks used
    - Web framework == fastapi
    - Database == MongoDB
    - api == Foursquare (https://th.foursquare.com/developers/home)

Setup Instructions
    - git clone https://github.com/sadanon-ria/restaurant_backend.git
    - cd restaurant_backend
    - python -m venv venv
    - .\venv\Scripts\activate
    - pip install -r requirements.txt

Setup .env
    สร้างไฟล์ .env ในโฟลเดอร์ "restaurant_backend/" โดยมีตัวแปรดังนี้
                        *** ส่วนของ API ***
    - url = "https://places-api.foursquare.com/places/search"
    - accept = "application/json"
    - X-Places-Api-Version = "2025-06-17"
    - authorization = "fsqXXXXXXXXXXXX" (ได้มาจาก api Foursquare)
                      *** ส่วนของ Database ***
    - dbUser = "your_username_mongodb"
    - dbPass = "your_password_mongodb"

Run the server
    - uvicorn main:app --reload

Test
    - http://127.0.0.1:8000/docs
    - Postman

Known Issues / Limitations
    - Foursquare API ใช้ฟรี แต่จำกัดการโควตา
    - รูปภาพอาจส่งค่า null กลับมาเนื่องจากโควตาหมด
    method |           endpoint           |   Description 
    'GET'  | '/dataDefault'               | แสดงผลร้านอาหารที่มีค่าเริ่มต้นคือ "บางซื่อ" 
    'GET'  | '/dataKey/{keyword}'         | ค้นหาร้านอาหารด้วย keyword จาก user 
    'GET'  | '/dataPhoto/{fsq_place_id}'  | ใช้ในการดึงข้อมูลรูปภาพ 
 
  
