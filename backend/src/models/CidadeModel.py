from src.configs.banco_de_dados import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class CidadeModel(Base):

    __tablename__ = "cidade"

    id_cidade = Column(Integer, primary_key=True, autoincrement=True)
    nome_cidade = Column(String(50), nullable=False)
    fk_id_estado = Column(Integer, ForeignKey("estado.id_estado"), nullable=False)

    estado = relationship("EstadoModel", back_populates="cidade")
    bairro = relationship("BairroModel", back_populates="cidade")

    def __init__(self, nome_cidade: str, id_estado: int) -> None:
        self.nome_cidade = nome_cidade
        self.fk_id_estado = id_estado

    def __repr__(self) -> str:
        return f"Cidade (id: {self.id_cidade}, nome: {self.nome_cidade}, id_estado: {self.fk_id_estado})"

    def to_dict(self) -> dict:
        return {
            "id_cidade": self.id_cidade,
            "nome_cidade": self.nome_cidade,
            "fk_id_estado": self.fk_id_estado,
        }
