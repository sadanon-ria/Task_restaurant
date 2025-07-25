from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from router.router import data

app = FastAPI()
app.include_router(data)

origins = [
    "http://localhost:8080",  
    "http://127.0.0.1:8080"
]

# Allow Vue frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

