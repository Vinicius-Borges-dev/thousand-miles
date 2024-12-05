from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.configs.banco_de_dados import Base


class VeiculoModel(Base):

    __tablename__ = "veiculo"

    id_veiculo = Column(Integer, primary_key=True, autoincrement=True)
    assentos = Column(Integer, nullable=False)
    preco_por_dia = Column(Integer, nullable=False)
    ano_fabricacao = Column(Integer, nullable=False)
    cor = Column(String(255), nullable=False)
    placa = Column(String(255), nullable=False)
    disponivel = Column(Integer, nullable=False)

    fk_id_categoria = Column(
        Integer, ForeignKey("categoria.id_categoria"), nullable=False
    )
    fk_id_cambio = Column(Integer, ForeignKey("cambio.id_cambio"), nullable=False)
    fk_id_combustivel = Column(
        Integer, ForeignKey("combustivel.id_combustivel"), nullable=False
    )
    fk_id_album_veiculo = Column(
        Integer, ForeignKey("album_veiculo.id_album_veiculo"), nullable=True
    )
    fk_id_modelo = Column(Integer, ForeignKey("modelo.id_modelo"), nullable=False)

    categoria = relationship("CategoriaModel", back_populates="veiculo")
    cambio = relationship("CambioModel", back_populates="veiculo")
    combustivel = relationship("CombustivelModel", back_populates="veiculo")
    album_veiculo = relationship("AlbumVeiculoModel", back_populates="veiculo")
    modelo = relationship("ModeloModel", back_populates="veiculo")
    veiculo_reserva = relationship("VeiculoReservaModel", back_populates="veiculo")
    favorito = relationship("FavoritoModel", back_populates="veiculo")

    def __init__(
        self,
        assentos: int,
        preco_por_dia: int,
        ano_fabricacao: int,
        cor: str,
        placa: str,
        disponivel: int,
    ) -> None:
        self.assentos = assentos
        self.preco_por_dia = preco_por_dia
        self.ano_fabricacao = ano_fabricacao
        self.cor = cor
        self.placa = placa
        self.disponivel = disponivel

    def __repr__(self) -> str:
        return f"Veiculo (id: {self.id_veiculo}, placa: {self.placa})"

    def to_dict(self) -> dict:
        return {
            "id_veiculo": self.id_veiculo,
            "assentos": self.assentos,
            "preco_por_dia": self.preco_por_dia,
            "ano_fabricacao": self.ano_fabricacao,
            "cor": self.cor,
            "placa": self.placa,
            "disponivel": self.disponivel,
            "categoria": self.categoria,
            "cambio": self.cambio,
            "combustivel": self.combustivel,
            "modelo": self.modelo,
        }
