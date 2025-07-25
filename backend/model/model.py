from pydantic import BaseModel
from datetime import datetime, Field
from typing import  Optional

class dataKeyword(BaseModel):
    keyword: str
    results: list[dict]
    timestamp: datetime = Field(default_factory=datetime.utcnow)