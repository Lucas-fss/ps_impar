import uvicorn
from fastapi import FastAPI
from api.routes import car_routes
from .config import DATABASE_URL
from .database.connection_database import Database 

Database(DATABASE_URL)

app = FastAPI()


app.include_router(car_routes.route, prefix="/cars", tags=["cars"])

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, host="0.0.0.0")