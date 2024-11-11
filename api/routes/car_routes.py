from fastapi import APIRouter
from api.schemas import CarSchema
route = APIRouter()

@route.post("/new_car",
            responses={
        200: {"description": "Usuário criado com sucesso!"},
        
    })
def add_new_car(car: CarSchema) -> str:
    try:
        pass
    except:
        pass
    else:
        return "success"
