from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src.configs.banco_de_dados import Base


class CategoriaModel(Base):

    __tablename__ = "categoria"

    id_categoria = Column(Integer, primary_key=True, autoincrement=True)
    nome_categoria = Column(String(50), nullable=False)

    veiculo = relationship("VeiculoModel", back_populates="categoria")

    def __init__(self, nome_categoria: str) -> None:
        self.nome_categoria = nome_categoria

    def __repr__(self) -> str:
        return f"Categoria (id: {self.id_categoria}, nome_categoria: {self.nome_categoria})"

    def to_dict(self) -> dict:
        return {
            "id_categoria": self.id_categoria,
            "nome_categoria": self.nome_categoria,
        }
