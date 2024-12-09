from src.configs.banco_de_dados import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class MarcaModel(Base):
    
    __tablename__ = "marca"
    
    id_marca = Column(Integer, primary_key=True, autoincrement=True)
    nome_marca = Column(String(50), nullable=False)
    logo_marca = Column(String(255), nullable=False)
    
    modelo = relationship('ModeloModel', back_populates='marca')
    
    def __init__(self, nome_marca:str, logo_marca:str)->None:
        self.nome_marca = nome_marca
        self.logo_marca = logo_marca
    
    def __repr__(self)->str:
        return f'Marca (id: {self.id_marca}, nome_marca: {self.nome_marca}, logo_marca: {self.logo_marca})'
    
    def to_dict(self)->dict:
        return {
            'id_marca': self.id_marca,
            'nome_marca': self.nome_marca,
            'logo_marca': self.logo_marca
        }