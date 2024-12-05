from database.db import Base
from sqlalchemy import Column, Integer, String , Boolean

class Printer(Base):
    __tablename__ = 'printers'
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    ip = Column(String, unique=True , nullable=False)
    mac = Column(String, unique=True , nullable=False)
    activo = Column(Boolean, default=True)
    tipo = Column(String, nullable=False)

