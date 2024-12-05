from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from src.configs.banco_de_dados import Base


class UsuarioModel(Base):

    __tablename__ = "usuario"

    id_usuario = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(100), nullable=False)
    senha = Column(String(255), nullable=False)
    nivel_acesso = Column(String(20), nullable=False)

    fk_id_dados_pessoais = Column(
        Integer, ForeignKey("dados_pessoais.id_dados_pessoais"), nullable=False
    )
    fk_id_endereco = Column(Integer, ForeignKey("endereco.id_endereco"), nullable=False)

    dados_pessoais = relationship("DadosPessoaisModel", back_populates="usuario")
    usuario_reserva = relationship("UsuarioReservaModel", back_populates="usuario")
    endereco = relationship("EnderecoModel", back_populates="usuario")
    favorito = relationship("FavoritoModel", back_populates="usuario")

    
    def __init__(self, email:str, senha:str, nivel_acesso:str, fk_id_dados_pessoais:int, fk_id_endereco:int)->None:
        self.email = email
        self.senha = senha
        self.nivel_acesso = nivel_acesso
        self.fk_id_dados_pessoais = fk_id_dados_pessoais
        self.fk_id_endereco = fk_id_endereco
    
    def __repr__(self)->str:
        return f"UsuarioModel (id_usuario: {self.id_usuario}, email: {self.email}, nivel_acesso: {self.nivel_acesso})"
    
    def to_dict(self):
        return {
            "id_usuario": self.id_usuario,
            "email": self.email,
            "nivel_acesso": self.nivel_acesso,
            "fk_id_dados_pessoais": self.fk_id_dados_pessoais,
            "fk_id_endereco": self.fk_id_endereco
        }