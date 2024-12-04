from src.configs.banco_de_dados import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class AlbumVeiculo(Base):
    
    __tablename__ = "album_veiculo"
    
    id_album_veiculo = Column(Integer, primary_key=True, autoincrement=True)
    foto_principal = Column(String(255), nullable=False)
    foto_secundaria = Column(String(255), nullable=False)
    foto_apresentacao_primaria = Column(String(255), nullable=False)
    foto_apresentacao_secundaria = Column(String(255), nullable=False)
    foto_apresentacao_terciaria = Column(String(255), nullable=False)
    
    modelo = relationship("ModeloModel", back_populates="album_veiculo")
    veiculo = relationship("VeiculoModel", back_populates="album_veiculo")