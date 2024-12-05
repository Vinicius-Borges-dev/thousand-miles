from sqlalchemy import Column, Integer, PrimaryKeyConstraint, ForeignKey
from sqlalchemy.orm import relationship
from src.configs.banco_de_dados import Base

class UsuarioReservaModel(Base):
    
    __tablename__ = "usuario_reserva"
    
    fk_id_reserva = Column(Integer, ForeignKey("reserva.id_reserva"), nullable=False)
    fk_id_usuario = Column(Integer, ForeignKey("usuario.id_usuario"), nullable=False)
    
    __table_args__ = (PrimaryKeyConstraint("fk_id_reserva", "fk_id_usuario"),)
    
    reserva = relationship("ReservaModel", back_populates="usuario_reserva")
    usuario = relationship("UsuarioModel", back_populates="usuario_reserva")

    def __init__(self, fk_id_reserva:int, fk_id_usuario:int)->None:
        self.fk_id_reserva = fk_id_reserva
        self.fk_id_usuario = fk_id_usuario
    
    def __repr__(self)->str:
        return f"UsuarioReserva (id_reserva: {self.fk_id_reserva}, id_usuario: {self.fk_id_usuario})"
    
    def to_dict(self)->dict:
        return {
            "fk_id_reserva": self.fk_id_reserva,
            "fk_id_usuario": self.fk_id_usuario
        }