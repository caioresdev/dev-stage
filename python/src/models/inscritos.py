from src.models.config_base import Base
from sqlalchemy import Column, Integer, String, ForeignKey

class Inscritos (Base):
    __tablename__ = 'Inscritos'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    email = Column(String, nullable=False)
    link = Column(String, nullable=True)
    evento_id = Column(Integer, ForeignKey('Eventos.id'))