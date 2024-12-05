from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from src.configs.banco_de_dados import Base

class SeguroModel(Base):
    
    __tablename__ = "seguro"
    
    id_seguro = Column(Integer, primary_key=True, autoincrement=True)
    tipo_seguro = Column(String(50), nullable=False)
    custo = Column(Float, nullable=False)
    
    reserva = relationship("ReservaModel", back_populates="seguro")
    
    def __init__(self, tipo_seguro:str, custo:float)->None:
        self.tipo_seguro = tipo_seguro
        self.custo = custo
    
    def __repr__(self)->str:
        return f"Seguro (id: {self.id_seguro}, tipo: {self.tipo_seguro}, custo: {self.custo})"
    
    def to_dict(self)->dict:
        return{
            "id_seguro": self.id_seguro,
            "tipo_seguro": self.tipo_seguro,
            "custo": self.custo
        }