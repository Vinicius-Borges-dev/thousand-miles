from src.models import MarcaModel
from sqlalchemy.exc import SQLAlchemyError
from flask import current_app as app


class MarcaService:

    def criar_marca(self, dados: dict):
        try:
            marca = MarcaModel(
                nome_marca=dados.get("nome_marca"), logo_marca=dados.get("logo_marca")
            )
            app.session.add(marca)
            app.session.commit()

            return marca
        except SQLAlchemyError as erro:
            app.session.rollback()
            raise erro

    def buscar_todas_marcas(self):
        try:
            marcas = app.session.query(MarcaModel).all()
            return marcas
        except SQLAlchemyError as erro:
            raise erro

    def buscar_marca_por_id(self, id_marca: int):
        try:
            marca = app.session.query(MarcaModel).filter_by(id_marca=id_marca).first()
            return marca
        except SQLAlchemyError as erro:
            raise erro

    def buscar_marca_por_nome(self, nome_marca: str):
        try:
            marca = (
                app.session.query(MarcaModel).filter_by(nome_marca=nome_marca).first()
            )
            return marca
        except SQLAlchemyError as erro:
            raise erro

    def atualizar_marca(self, id_marca: int, dados: dict):
        try:
            marca = app.session.query(MarcaModel).filter_by(id_marca=id_marca).first()
            marca.nome_marca = dados.get("nome_marca")
            marca.logo_marca = dados.get("logo_marca")
            app.session.commit()

            return marca
        except SQLAlchemyError as erro:
            app.session.rollback()
            raise erro

    def deletar_marca(self, id_marca: int):
        try:
            marca = app.session.query(MarcaModel).filter_by(id_marca=id_marca).first()
            app.session.delete(marca)
            app.session.commit()
        except SQLAlchemyError as erro:
            app.session.rollback()
            raise erro
