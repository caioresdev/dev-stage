from src.models.config_base import Base
from sqlalchemy import Column, Integer, String

class Eventos (Base):
    __tablename__ = 'Eventos'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)