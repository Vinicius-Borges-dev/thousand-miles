from src.models import CombustivelModel
from sqlalchemy.exc import SQLAlchemyError
from flask import current_app as app


class CombustivelService:

    def criar_combustivel(self, dados: dict):
        try:
            combustivel = CombustivelModel(
                tipo_combustivel=dados.get("tipo_combustivel")
            )
            app.session.add(combustivel)
            app.session.commit()

            return combustivel
        except SQLAlchemyError as erro:
            app.session.rollback()
            raise erro

    def buscar_todos_combustiveis(self):
        try:
            combustiveis = app.session.query(CombustivelModel).all()
            return combustiveis
        except SQLAlchemyError as erro:
            raise erro

    def buscar_combustivel_por_id(self, id_combustivel: int):
        try:
            combustivel = (
                app.session.query(CombustivelModel)
                .filter_by(id_combustivel=id_combustivel)
                .first()
            )
            return combustivel
        except SQLAlchemyError as erro:
            raise erro

    def buscar_combustivel_por_nome(self, nome_combustivel: str):
        try:
            combustivel = (
                app.session.query(CombustivelModel)
                .filter_by(tipo_combustivel=nome_combustivel)
                .first()
            )
            return combustivel
        except SQLAlchemyError as erro:
            raise erro

    def atualizar_combustivel(self, id_combustivel: int, dados: dict):
        try:
            combustivel = (
                app.session.query(CombustivelModel)
                .filter_by(id_combustivel=id_combustivel)
                .first()
            )
            combustivel.tipo_combustivel = dados.get("tipo_combustivel")
            app.session.commit()

            return combustivel
        except SQLAlchemyError as erro:
            app.session.rollback()
            raise erro

    def deletar_combustivel(self, id_combustivel: int):
        try:
            combustivel = (
                app.session.query(CombustivelModel)
                .filter_by(id_combustivel=id_combustivel)
                .first()
            )
            app.session.delete(combustivel)
            app.session.commit()
        except SQLAlchemyError as erro:
            app.session.rollback()
            raise erro

    def buscar_por_nome_semelhante(self, nome_combustivel: str):
        try:
            combustiveis = (
                app.session.query(CombustivelModel)
                .filter(CombustivelModel.tipo_combustivel.like(f"%{nome_combustivel}%"))
                .all()
            )
            return combustiveis
        except SQLAlchemyError as erro:
            raise erro