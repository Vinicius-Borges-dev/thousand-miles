from src.configs.banco_de_dados import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class DocumentoModel(Base):
    
    __tablename__ = "documento"
    
    id_documento = Column(Integer, primary_key=True, autoincrement=True)
    cpf = Column(String(11), nullable=False)
    rg = Column(String(9), nullable=False)
    
    dados_pessoais = relationship('DadosPessoaisModel', back_populates='documento')
    
    def __init__(self, tipo_documento:str, numero_documento:str)->None:
        self.tipo_documento = tipo_documento
        self.numero_documento = numero_documento
    
    def __repr__(self)->str:
        return f'Documento (id: {self.id_documento}, tipo_documento: {self.tipo_documento}, numero_documento: {self.numero_documento})'
    
    def to_dict(self)->dict:
        return {
            'id_documento': self.id_documento,
            'tipo_documento': self.tipo_documento,
            'numero_documento': self.numero_documento
        }