from sqlalchemy import Column, Integer, String, ForeignKey, Date, Float
from sqlalchemy.orm import relationship
from src.configs.banco_de_dados import Base


class ReservaModel(Base):

    __tablename__ = "reserva"

    id_reserva = Column(Integer, primary_key=True, autoincrement=True)
    data_locacao = Column(Date, nullable=False)
    data_devolucao = Column(Date, nullable=False)
    preco_total = Column(Float, nullable=False)
    status = Column(String(20), nullable=False)
    fk_id_seguro = Column(Integer, ForeignKey("seguro.id_seguro"), nullable=False)

    seguro = relationship("SeguroModel", back_populates="reserva")
    veiculo_reserva = relationship("VeiculoReservaModel", back_populates="reserva")
    usuario_reserva = relationship("UsuarioReservaModel", back_populates="reserva")

    def __init__(
        self,
        data_locacao: str,
        data_devolucao: str,
        preco_total: float,
        status: str,
        fk_id_seguro: int,
    ) -> None:
        self.data_locacao = data_locacao
        self.data_devolucao = data_devolucao
        self.preco_total = preco_total
        self.status = status
        self.fk_id_seguro = fk_id_seguro

    def __repr__(self) -> str:
        return f"Reserva (id: {self.id_reserva}, data_locação: {self.data_locacao}, data_devolução: {self.data_devolucao}, preco: {self.preco_total}, status: {self.status})"
    
    def to_dict(self)->dict:
        return {
            "id_reserva": self.id_reserva,
            "data_locacao": self.data_locacao,
            "data_devolucao": self.data_devolucao,
            "preco_total": self.preco_total,
            "status": self.status,
            "fk_id_seguro": self.fk_id_seguro,
        }
