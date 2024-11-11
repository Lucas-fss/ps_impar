from .connection_database import Database
from api.models.model import Cars, Photos

from api.config import DATABASE_URL
db = Database(DATABASE_URL)
class Photo:
    @classmethod
    def add_new_photo(cls, base_64: str) -> int:
        session = db.get_session()
        new_photo = Photos(base=str(base_64))
        session.add(new_photo)
        session.commit()
        return new_photo.id        

class Car:
    _session = db.get_session()

    @classmethod
    def add_new_car(cls, name: str, status: str, photo_id: int) -> None:
        new_car = Cars(name=name, status=status, photo_id=photo_id)
        cls._session.session.add(new_car)
        cls._session.session.commit()

    @classmethod
    def remove_car(cls, car_id: int) -> None:
        car = cls._session.query(Cars).get(car_id)
        if car:
            cls._session.delete(car)
            cls._session.commit()