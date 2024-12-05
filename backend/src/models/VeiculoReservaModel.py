from sqlalchemy import Column, Integer, PrimaryKeyConstraint, ForeignKey
from sqlalchemy.orm import relationship
from src.configs.banco_de_dados import Base

class VeiculoReservaModel(Base):
    
    __tablename__ = "veiculo_reserva"
    
    fk_id_veiculo = Column(Integer, ForeignKey("veiculo.id_veiculo"), nullable=False)
    fk_id_reserva = Column(Integer, ForeignKey("reserva.id_reserva"), nullable=False)
    
    __table_args__ = (PrimaryKeyConstraint("fk_id_veiculo", "fk_id_reserva"),)
    
    veiculo = relationship("VeiculoModel", back_populates="veiculo_reserva")
    reserva = relationship("ReservaModel", back_populates="veiculo_reserva")
    
    def __init__(self, fk_id_veiculo:int, fk_id_reserva:int)->None:
        self.fk_id_reserva = fk_id_reserva
        self.fk_id_veiculo = fk_id_veiculo
    
    def __repr__(self)->str:
        return f"VeiculoReserva (id_veiculo: {self.fk_id_veiculo}, id_reserva: {self.fk_id_reserva})"
    
    def to_dict(self)->dict:
        return {
            "fk_id_veiculo": self.fk_id_veiculo,
            "fk_id_reserva": self.fk_id_reserva
        }