from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from api.database.connection_database import Base

class Photos(Base):
    __tablename__ = "photo"
    id = Column(Integer, primary_key=True, index=True)
    base = Column(String)

class Cars(Base):
    __tablename__ = "car"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    status = Column(String)

    photo_id = Column(Integer, ForeignKey("photo.id")) 
    photo = relationship("Photos", backref="car", cascade="all, delete")