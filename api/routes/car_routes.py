from fastapi import APIRouter, UploadFile, Depends, HTTPException, Form, File
from base64 import b64encode
from api.schemas import CarSchema
from api.database.crud import Photo, Car
from typing import Optional
route = APIRouter()

@route.post("/new",
            responses={
                200: {"description": "Carro adicionado com sucesso!"},
        })
async def add_new_car(file: UploadFile, car: CarSchema = Depends()) -> str:
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
                    200: {"description": "Carro removido com sucesso!"},
                    404: {"description": "Carro não encontrado!"}
            })
def remove_car(car_id: int) -> str:
    try:
        Car.remove_car(car_id=car_id)
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    else:
        return "success"
    

@route.put("/change/{car_id}", 
            responses={
                200: {"description": "Carro atualizado com sucesso!"},
                404: {"description": "Carro não encontrado!"}
        })
async def change_car_info(car_id: int, name = Form(None), status = Form(None) , file: Optional[UploadFile] = File(None)) -> str:
    try:
        photo_id = None
        if file:
            file_content = await file.read()
            encode = b64encode(file_content).decode('utf-8')
            photo_id = Photo.add_new_photo(encode)
            
        Car.change_car(car_id, name, status, photo_id)
        
        
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    else:
        return "success"