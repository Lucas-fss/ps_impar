from pydantic import BaseModel
from typing import Optional
from fastapi import UploadFile

class CarSchema(BaseModel):
    Name:  str 
    Status: str 
