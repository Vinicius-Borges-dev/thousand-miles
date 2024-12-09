from src.models import ModeloModel
from sqlalchemy.exc import SQLAlchemyError
from flask import current_app as app


class ModeloService:

    def criar_modelo(self, dados: dict):
        try:
            modelo = ModeloModel(
                fk_id_album_veiculo=dados.get("id_album_veiculo"),
                fk_id_marca=dados.get("id_marca"),
                nome_modelo=dados.get("nome_modelo"),
            )
            app.session.add(modelo)
            app.session.commit()

            return modelo
        except SQLAlchemyError as erro:
            app.session.rollback()
            raise erro

    def buscar_todos_modelos(self):
        try:
            modelos = app.session.query(ModeloModel).all()
            return modelos
        except SQLAlchemyError as erro:
            raise erro

    def buscar_modelo_por_id(self, id_modelo: int):
        try:
            modelo = (
                app.session.query(ModeloModel).filter_by(id_modelo=id_modelo).first()
            )
            return modelo
        except SQLAlchemyError as erro:
            raise erro

    def buscar_modelo_por_nome(self, nome_modelo: str):
        try:
            modelo = (
                app.session.query(ModeloModel)
                .filter_by(nome_modelo=nome_modelo)
                .first()
            )
            return modelo
        except SQLAlchemyError as erro:
            raise erro

    def atualizar_modelo(self, id_modelo: int, dados: dict):
        try:
            modelo = (
                app.session.query(ModeloModel).filter_by(id_modelo=id_modelo).first()
            )
            modelo.fk_id_album_veiculo = dados.get("id_album_veiculo")
            modelo.fk_id_marca = dados.get("id_marca")
            modelo.nome_modelo = dados.get("nome_modelo")
            app.session.commit()

            return modelo
        except SQLAlchemyError as erro:
            app.session.rollback()
            raise erro

    def deletar_modelo(self, id_modelo: int):
        try:
            modelo = (
                app.session.query(ModeloModel).filter_by(id_modelo=id_modelo).first()
            )
            app.session.delete(modelo)
            app.session.commit()
        except SQLAlchemyError as erro:
            app.session.rollback()
            raise erro

    def buscar_nome_semelhate(self, nome_modelo: str):
        try:
            modelos = (
                app.session.query(ModeloModel)
                .filter(ModeloModel.nome_modelo.like(f"%{nome_modelo}%"))
                .all()
            )
            return modelos
        except SQLAlchemyError as erro:
            raise erro
