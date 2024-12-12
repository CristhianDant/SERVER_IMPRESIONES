from database.db import Base
from sqlalchemy import Column, Integer, String , Boolean
from pydantic import BaseModel , Field


class Printer_database(Base):
    __tablename__ = 'printers'
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    ip = Column(String, unique=True , nullable=False)
    mac = Column(String, unique=True , nullable=False)
    activo = Column(Boolean, default=True)
    name_printer = Column(String, default="No name")
    tipo = Column(String, nullable=False)


class Printer(BaseModel):
    id: int
    ip: str
    mac: str
    activo: bool
    name_printer: str
    tipo: str

    class Config:
        from_attributes = True

