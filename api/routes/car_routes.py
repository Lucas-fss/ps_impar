from fastapi import APIRouter, UploadFile, File, Depends
from base64 import b64encode
from api.schemas import CarSchema
from api.database.crud import Photo, Car
route = APIRouter()

@route.post("/new",
            responses={
                200: {"description": "Carro adicionado com sucesso!"},
        })
async def add_new_car(file: UploadFile, car: CarSchema = Depends()):
    try:

        file_content = await file.read()
        encode = b64encode(file_content).decode('utf-8')
        photo_id = Photo.add_new_photo(encode)
        Car.add_new_car(name=car.Name, status=car.Status, photo_id=photo_id)
    except Exception as e:
        return f'error: {e}'
    else:
        return "success"

@route.delete("/remove/{car_id}", 
                responses={
                    200: {"description": "Carro adicionado com sucesso!"},
            })
def remove_car(car_id: int) -> str:
    try:
        Car.remove_car(car_id=car_id)
    except Exception as e:
        return f'error: {e}'
    else:
        return "success"
    

@route.put("/change", 
            responses={
                200: {"description": "Carro adicionado com sucesso!"},
        })
def change_car_info(car: CarSchema):
    try:
        pass
    except Exception as e:
        return f'error: {e}'
    else:
        return "success"