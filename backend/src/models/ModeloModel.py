from src.configs.banco_de_dados import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class ModeloModel(Base):
    
    __tablename__ = "modelo"
