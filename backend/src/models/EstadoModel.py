from src.configs.banco_de_dados import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class EstadoModel(Base):
    
    __tablename__ = 'estado'
    
    id_estado = Column(Integer, primary_key=True, autoincrement=True)
    nome_estado = Column(String(50), nullable=False)
    
    cidade = relationship('CidadeModel', back_populates='estado')
    
    def __init__(self, nome_estado:str)->None:
        self.nome_estado = nome_estado

    def __repr__(self)->str:
        return f'Estado (id: {self.id_estado}, nome_estado: {self.nome_estado})'

    def to_dict(self)->dict:
        return {
            'id_estado': self.id_estado,
            'nome_estado': self.nome_estado
        }