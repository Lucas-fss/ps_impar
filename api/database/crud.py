from .connection_database import Database
from api.models.model import Car, Photo

from api.config import DATABASE_URL

class Photo:
    @classmethod
    def add_new_phot(cls, base_64: str) -> int:
        session = Database.get_session()
        new_photo = Photo(base_64=base_64)
        session.add(new_photo)
        session.commit()
        return new_photo.id        

class Cars:
    @classmethod
    def add_new_car(cls, name: str, status: str, photo_id: int) -> None:
        session = Database.get_session()
        new_car = Car(name=name, status=status, photo_id=photo_id)
        session.add(new_car)
        session.commit()
