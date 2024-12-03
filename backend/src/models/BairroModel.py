from src.configs.banco_de_dados import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class BairroModel(Base):
    
    __tablename__ = 'bairro'
    
    id_bairro = Column(Integer, primary_key=True, autoincrement=True)
    nome_bairro = Column(String(50), nullable=False)
    fk_id_cidade = Column(Integer, ForeignKey('cidade.id_cidade'), nullable=False)
    
    cidade = relationship('CidadeModel', back_populates='bairro')
    endereco = relationship('EnderecoModel', back_populates='bairro')
    
    def __init__(self, nome_bairro:str, fk_id_cidade:int)->None:
        self.nome_bairro = nome_bairro
        self.fk_id_cidade = fk_id_cidade

    def __repr__(self)->str:
        return f'Bairro (id: {self.id_bairro}, nome_bairro: {self.nome_bairro})'
    
    def to_dict(self)->dict:
        return {
            'id_bairro': self.id_bairro,
            'nome_bairro': self.nome_bairro,
            'fk_id_cidade': self.fk_id_cidade
        }