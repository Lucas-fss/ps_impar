import uvicorn
from fastapi import FastAPI
from api.routes import car_routes
from api.routes import photo_routes
app = FastAPI()


app.include_router(car_routes.route, prefix="/cars", tags=["cars"])
app.include_router(photo_routes.route_photo, prefix="/photos", tags=["photos"])
if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, host="0.0.0.0")