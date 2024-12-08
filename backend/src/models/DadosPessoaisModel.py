from src.configs.banco_de_dados import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship


class DadosPessoaisModel(Base):

    __tablename__ = "dados_pessoais"

    id_dados_pessoais = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50), nullable=False)
    sobrenome = Column(String(50), nullable=False)
    data_nascimento = Column(Date, nullable=True)
    fk_id_documento = Column(
        Integer, ForeignKey("documento.id_documento", ondelete="CASCADE"), nullable=False
    )

    documento = relationship("DocumentoModel", back_populates="dados_pessoais")
    usuario = relationship("UsuarioModel", back_populates="dados_pessoais", cascade="all, delete-orphan")

    def __init__(self, nome: str, sobrenome: str, fk_id_documento: int, data_nascimento:str) -> None:
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento
        self.fk_id_documento = fk_id_documento

    def __repr__(self) -> str:
        return f"DadosPessoais (id: {self.id_dados_pessoais}, nome: {self.nome}, sobrenome: {self.sobrenome})"

    def to_dict(self) -> dict:
        return {
            "id_dados_pessoais": self.id_dados_pessoais,
            "nome": self.nome,
            "sobrenome": self.sobrenome,
            "fk_id_documento": self.fk_id_documento,
        }
