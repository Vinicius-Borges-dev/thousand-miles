from src.configs.banco_de_dados import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class ModeloModel(Base):
    
    __tablename__ = "modelo"

    id_modelo = Column(Integer, primary_key=True, autoincrement=True)
    nome_modelo = Column(String(50), nullable=False)
    fk_id_marca = Column(Integer, ForeignKey("marca.id_marca"), nullable=False)
    fk_id_album_veiculo = Column(Integer, ForeignKey("album_veiculo.id_album_veiculo"), nullable=False)
    
    marca = relationship("MarcaModel", back_populates="modelo")
    album_veiculo = relationship("AlbumVeiculoModel", back_populates="modelo")
    veiculo = relationship("VeiculoModel", back_populates="modelo")
    
    def __init__(self, nome_modelo:str, fk_id_marca:int, fk_id_album_veiculo:int)->None:
        self.nome_modelo = nome_modelo
        self.fk_id_marca = fk_id_marca
        self.fk_id_album_veiculo = fk_id_album_veiculo
    
    def __repr__(self)->str:
        return f'Modelo (id: {self.id_modelo}, nome_modelo: {self.nome_modelo})'

    def to_dict(self)->dict:
        return {
            'id_modelo': self.id_modelo,
            'nome_modelo': self.nome_modelo,
            'fk_id_marca': self.fk_id_marca,
            'fk_id_album_veiculo': self.fk_id_album_veiculo
        }