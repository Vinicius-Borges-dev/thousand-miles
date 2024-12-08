from src.configs.banco_de_dados import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class EnderecoModel(Base):
    
    __tablename__ = 'endereco'
    
    id_endereco = Column(Integer, primary_key=True, autoincrement=True)
    rua = Column(String(50), nullable=False)
    numero = Column(Integer, nullable=False)
    fk_id_bairro = Column(Integer, ForeignKey('bairro.id_bairro'), nullable=False)
    
    bairro = relationship('BairroModel', back_populates='endereco')
    usuario = relationship('UsuarioModel', back_populates='endereco', cascade="all, delete-orphan")
    
    def __init__(self, rua:str, numero:int, fk_id_bairro:int)->None:
        self.rua = rua
        self.numero = numero
        self.fk_id_bairro = fk_id_bairro
    
    def __repr__(self)->str:
        return f'Endereco (id: {self.id_endereco}, rua: {self.rua}, numero: {self.numero})'
    
    def to_dict(self)->dict:
        return {
            'id_endereco': self.id_endereco,
            'rua': self.rua,
            'numero': self.numero,
            'fk_id_bairro': self.fk_id_bairro
        }