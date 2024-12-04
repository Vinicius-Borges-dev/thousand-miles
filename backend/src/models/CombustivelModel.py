from src.configs.banco_de_dados import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class CombustivelModel(Base):
    
    __tablename__ = "combustivel"
    
    id_combustivel = Column(Integer, primary_key=True, autoincrement=True)
    tipo_combustivel = Column(String(50), nullable=False)
    
    veiculo = relationship("VeiculoModel", back_populates="combustivel")
    
    def __init__(self, tipo_combustivel:str)->None:
        self.tipo_combustivel = tipo_combustivel
    
    def __repr__(self)->str:
        return f'Combustivel (id: {self.id_combustivel}, tipo_combustivel: {self.tipo_combustivel})'
    
    def to_dict(self)->dict:
        return {
            'id_combustivel': self.id_combustivel,
            'tipo_combustivel': self.tipo_combustivel
        }