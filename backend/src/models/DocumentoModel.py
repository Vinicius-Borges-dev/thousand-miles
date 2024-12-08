from src.configs.banco_de_dados import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class DocumentoModel(Base):
    
    __tablename__ = "documento"
    
    id_documento = Column(Integer, primary_key=True, autoincrement=True)
    cpf = Column(String(11), nullable=False)
    rg = Column(String(9), nullable=False)
    
    dados_pessoais = relationship('DadosPessoaisModel', back_populates='documento', cascade="all, delete-orphan")
    
    def __init__(self, cpf:str, rg:str)->None:
        self.cpf = cpf
        self.rg = rg
    
    def __repr__(self)->str:
        return f'Documento (id: {self.id_documento}, cpf: {self.cpf}, rg: {self.rg})'
    
    def to_dict(self)->dict:
        return {
            'id_documento': self.id_documento,
            'cpf': self.cpf,
            'rg': self.rg
        }