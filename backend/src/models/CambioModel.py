from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src.configs.banco_de_dados import Base

class CambioModel(Base):
    
    __tablename__ = "cambio"
    
    id_cambio = Column(Integer, primary_key=True, autoincrement=True)
    tipo_cambio = Column(String(50), nullable=False)
    
    veiculo = relationship("VeiculoModel", back_populates="cambio")
    
    def __init__(self, tipo_cambio:str)->None:
        self.tipo_cambio = tipo_cambio
    
    def __repr__(self)->str:
        return f'Cambio (id: {self.id_cambio}, tipo_cambio: {self.tipo_cambio})'
    
    def to_dict(self)->dict:
        return {
            'id_cambio': self.id_cambio,
            'tipo_cambio': self.tipo_cambio
        }
        