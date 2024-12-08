from flask import current_app as app
from sqlalchemy.exc import SQLAlchemyError
from src.models import UsuarioModel


class UsuarioService:

    def criar_usuario(self, dados: dict):
        try:
            novo_usuario = UsuarioModel(
                email=dados.get("email"),
                senha=dados.get("senha"),
                nivel_acesso=dados.get("nivel_acesso"),
                fk_id_dados_pessoais=dados.get("id_dados_pessoais"),
                fk_id_endereco=dados.get("id_endereco"),
            )

            app.session.add(novo_usuario)
            app.session.commit()

            return novo_usuario
        except SQLAlchemyError as erro:
            app.session.rollback()
            raise erro

    def editar_usuario(self, id_usuario: int, dados: dict):
        try:
            usuario = app.session.query(UsuarioModel).filter_by(id_usuario=id_usuario).first()

            usuario.email = dados.get("email")
            usuario.senha = dados.get("senha")
            usuario.nivel_acesso = dados.get("nivel_acesso")
            usuario.fk_id_dados_pessoais = dados.get("id_dados_pessoais")
            usuario.fk_id_endereco = dados.get("id_endereco")

            app.session.commit()

            return usuario
        except SQLAlchemyError as erro:
            app.session.rollback()
            raise erro
    
    def deletar_usuario(self, id_usuario: int):
        try:
            usuario = app.session.query(UsuarioModel).filter_by(id_usuario=id_usuario).first()
            
            app.session.delete(usuario)
            app.session.commit()
            
            return True
        except SQLAlchemyError as erro:
            app.session.rollback()
            raise erro
    
    def capturar_informacoes_usuario(self, id_usuario: int):
        try:
            usuario = app.session.query(UsuarioModel).filter_by(id_usuario=id_usuario).first()
            return usuario
        except SQLAlchemyError as erro:
            raise erro
    
    def buscar_todos_usuarios(self):
        try:
            usuarios = app.session.query(UsuarioModel).all()
            return usuarios
        except SQLAlchemyError as erro:
            raise erro
    
    def verificar_email(self, email: str):
        try:
            usuario = app.session.query(UsuarioModel).filter_by(email=email).first()
            return usuario
        except SQLAlchemyError as erro:
            raise erro