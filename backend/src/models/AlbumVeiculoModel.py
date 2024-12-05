from src.configs.banco_de_dados import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class AlbumVeiculoModel(Base):

    __tablename__ = "album_veiculo"

    id_album_veiculo = Column(Integer, primary_key=True, autoincrement=True)
    foto_principal = Column(String(255), nullable=False)
    foto_secundaria = Column(String(255), nullable=False)
    foto_apresentacao_primaria = Column(String(255), nullable=False)
    foto_apresentacao_secundaria = Column(String(255), nullable=False)
    foto_apresentacao_terciaria = Column(String(255), nullable=False)

    modelo = relationship("ModeloModel", back_populates="album_veiculo")
    veiculo = relationship("VeiculoModel", back_populates="album_veiculo")

    def __init__(
        self,
        foto_principal: str,
        foto_secundaria: str,
        foto_apresentacao_primaria: str,
        foto_apresentacao_secundaria: str,
        foto_apresentacao_terciaria: str,
    ) -> None:
        self.foto_principal = foto_principal
        self.foto_secundaria = foto_secundaria
        self.foto_apresentacao_primaria = foto_apresentacao_primaria
        self.foto_apresentacao_secundaria = foto_apresentacao_secundaria
        self.foto_apresentacao_terciaria = foto_apresentacao_terciaria

    def __repr__(self) -> str:
        return f"AlbumVeiculo (id: {self.id_album_veiculo}, foto_principal: {self.foto_principal})"

    def to_dict(self) -> dict:
        return {
            "id_album_veiculo": self.id_album_veiculo,
            "foto_principal": self.foto_principal,
            "foto_secundaria": self.foto_secundaria,
            "foto_apresentacao_primaria": self.foto_apresentacao_primaria,
            "foto_apresentacao_secundaria": self.foto_apresentacao_secundaria,
            "foto_apresentacao_terciaria": self.foto_apresentacao_terciaria,
        }
