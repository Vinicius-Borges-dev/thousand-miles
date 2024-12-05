from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from src.configs.banco_de_dados import Base


class FavoritoModel(Base):

    __tablename__ = "favorito"

    id_favorito = Column(Integer, primary_key=True, autoincrement=True)
    fk_id_usuario = Column(Integer, ForeignKey("usuario.id_usuario"), nullable=False)
    fk_id_veiculo = Column(Integer, ForeignKey("veiculo.id_veiculo"), nullable=False)

    usuario = relationship("UsuarioModel", back_populates="favorito")
    veiculo = relationship("VeiculoModel", back_populates="favorito")

    def __init__(self, fk_id_usuario, fk_id_veiculo):
        self.fk_id_usuario = fk_id_usuario
        self.fk_id_veiculo = fk_id_veiculo

    def __repr__(self):
        return f"FavoritoModel (id_favorito: {self.id_favorito}, fk_id_usuario: {self.fk_id_usuario}, fk_id_veiculo: {self.fk_id_veiculo})"

    def to_dict(self):
        return {
            "id_favorito": self.id_favorito,
            "fk_id_usuario": self.fk_id_usuario,
            "fk_id_veiculo": self.fk_id_veiculo,
        }
