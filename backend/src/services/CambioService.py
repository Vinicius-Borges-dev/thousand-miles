from src.models import CambioModel
from sqlalchemy.exc import SQLAlchemyError
from flask import current_app as app


class CambioService:

    def criar_cambio(self, dados: dict):
        try:
            cambio = CambioModel(tipo_cambio=dados.get("nome_cambio"))
            app.session.add(cambio)
            app.session.commit()

            return cambio
        except SQLAlchemyError as erro:
            app.session.rollback()
            raise erro

    def buscar_todos_cambios(self):
        try:
            cambios = app.session.query(CambioModel).all()
            return cambios
        except SQLAlchemyError as erro:
            raise erro

    def buscar_cambio_por_id(self, id_cambio: int):
        try:
            cambio = (
                app.session.query(CambioModel).filter_by(id_cambio=id_cambio).first()
            )
            return cambio
        except SQLAlchemyError as erro:
            raise erro

    def buscar_cambio_por_nome(self, nome_cambio: str):
        try:
            cambio = (
                app.session.query(CambioModel)
                .filter_by(tipo_cambio=nome_cambio)
                .first()
            )
            return cambio
        except SQLAlchemyError as erro:
            raise erro

    def atualizar_cambio(self, id_cambio: int, dados: dict):
        try:
            cambio = (
                app.session.query(CambioModel).filter_by(id_cambio=id_cambio).first()
            )
            cambio.tipo_cambio = dados.get("tipo_cambio")
            app.session.commit()

            return cambio
        except SQLAlchemyError as erro:
            app.session.rollback()
            raise erro

    def deletar_cambio(self, id_cambio: int):
        try:
            cambio = (
                app.session.query(CambioModel).filter_by(id_cambio=id_cambio).first()
            )
            app.session.delete(cambio)
            app.session.commit()
        except SQLAlchemyError as erro:
            app.session.rollback()
            raise erro

    def buscar_cambio_por_nome_semelhante(self, nome_cambio: str):
        try:
            cambios = (
                app.session.query(CambioModel)
                .filter(CambioModel.tipo_cambio.like(f"%{nome_cambio}%"))
                .all()
            )
            return cambios
        except SQLAlchemyError as erro:
            raise erro
