from .connection_database import Database
from api.models.model import Cars, Photos
from fastapi import HTTPException
from base64 import b64encode
from api.config import DATABASE_URL
db = Database(DATABASE_URL)

class Photo:
    _session = db.get_session()

    @classmethod
    def add_new_photo(cls, base_64: str) -> int:
        new_photo = Photos(base=str(base_64))
        cls._session.add(new_photo)
        cls._session.commit()
        return new_photo.id        
    
    @classmethod
    def remove_photo(cls, photo_id: int = None) -> None:
        try:
            photo = cls.get_photo(photo_id)
            cls._session.delete(photo)
            cls._session.commit()
        except HTTPException:
            raise  HTTPException(status_code=404, detail="Foto não encontrada!")
        
    @classmethod
    def get_photo(cls, photo_id: int = None) -> Photos:
        photo = cls._session.query(Photos).get(photo_id)
        if not photo:
            raise  HTTPException(status_code=404, detail="Foto não encontrada!")
        return photo

class Car:
    _session = db.get_session()

    @classmethod
    def add_new_car(cls, name: str, status: str, photo_id: int) -> None:
        new_car = Cars(name=name, status=status, photo_id=photo_id)
        cls._session.add(new_car)
        cls._session.commit()

    @classmethod
    def remove_car(cls, car_id: int) -> None:
        try:
            car = cls.get_car(car_id)
            cls._session.delete(car)
            cls._session.commit()
        except HTTPException:
            raise HTTPException(status_code=404, detail="Carro não encontrado!")
    
    @classmethod
    def change_car(cls, car_id: int = None, name: str = None, status: str = None, photo_id: int = None) -> None:
        try:
            car = cls.get_car(car_id)
            if name: 
                car.name = name

            if status: 
                car.status = status

            if photo_id: 
                Photo.remove_photo(car.photo_id)
                car.photo_id = photo_id
                
            cls._session.commit()
        except HTTPException:
            raise HTTPException(status_code=404, detail="Carro não encontrado!")
    
    @classmethod
    def get_car(cls, car_id: int = None) -> Cars:
        car = cls._session.query(Cars).get(car_id)
        if not car:
            raise HTTPException(status_code=404, detail="Carro não encontrado!")
        return car