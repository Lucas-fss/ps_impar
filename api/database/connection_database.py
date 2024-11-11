from sqlalchemy.orm import sessionmaker, scoped_session, declarative_base
from sqlalchemy import create_engine
from typing import Optional
from api.config import DATABASE_URL


Base = declarative_base()



class Database():
    _instance: Optional['Database'] = None
    def __new__(cls, db_path:str = None) -> 'Database':
        if not isinstance(cls._instance, Database):
            cls._instance = super(Database, cls).__new__(cls)
            cls.engine = create_engine(db_path, echo=True)
            cls._instance.Session = scoped_session(sessionmaker(bind=cls._instance.engine))

            from api.models.model import Car, Photo 
            Base.metadata.create_all(bind=cls.engine)
        return cls._instance
    
    def get_session(self) -> scoped_session:
        return self.Session()

    def close_current_session(self) -> None:
        self.Session.remove()

    def close_all_connections(self) -> None:
        self.Session.remove()
        self.engine.dispose()
