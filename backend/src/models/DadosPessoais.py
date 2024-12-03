from src.configs.banco_de_dados import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class DadosPessoaisModel(Base):
    
    __tablename__ = "dados_pessoais"
    
    id_dados_pessoais = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50), nullable=False)
    sobrenome = Column(String(50), nullable=False)
    fk_id_documento = Column(Integer, ForeignKey("documento.id_documento"), nullable=False)
    
    documento = relationship("DocumentoModel", back_populates="dados_pessoais")