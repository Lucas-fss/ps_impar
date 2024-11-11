from pydantic import BaseModel

class CarSchema(BaseModel):
    Name:  str
    Status: str
