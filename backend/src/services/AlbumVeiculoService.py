from src.models import AlbumVeiculoModel
from sqlalchemy.exc import SQLAlchemyError
from flask import current_app as app


class AlbumVeiculoService:

    def criar_album_veiculo(self, dados: dict):
        try:
            album_veiculo = AlbumVeiculoModel(
                foto_apresentacao_primaria=dados.get("foto_apresentacao_primaria"),
                foto_apresentacao_secundaria=dados.get("foto_apresentacao_secundaria"),
                foto_apresentacao_terciaria=dados.get("foto_apresentacao_terciaria"),
                foto_principal=dados.get("foto_principal"),
                foto_secundaria=dados.get("foto_secundaria"),
            )
            app.session.add(album_veiculo)
            app.session.commit()

            return album_veiculo
        except SQLAlchemyError as erro:
            app.session.rollback()
            raise erro

    def buscar_album_veiculo_por_id(self, id_album_veiculo: int):
        try:
            album_veiculo = (
                app.session.query(AlbumVeiculoModel)
                .filter_by(id_album_veiculo=id_album_veiculo)
                .first()
            )
            return album_veiculo
        except SQLAlchemyError as erro:
            raise erro

    def atualizar_album_veiculo(self, id_album_veiculo: int, dados: dict):
        try:
            album_veiculo = (
                app.session.query(AlbumVeiculoModel)
                .filter_by(id_album_veiculo=id_album_veiculo)
                .first()
            )
            album_veiculo.foto_apresentacao_primaria = dados.get(
                "foto_apresentacao_primaria"
            )
            album_veiculo.foto_apresentacao_secundaria = dados.get(
                "foto_apresentacao_secundaria"
            )
            album_veiculo.foto_apresentacao_terciaria = dados.get(
                "foto_apresentacao_terciaria"
            )
            album_veiculo.foto_principal = dados.get("foto_principal")
            album_veiculo.foto_secundaria = dados.get("foto_secundaria")
            app.session.commit()

            return album_veiculo
        except SQLAlchemyError as erro:
            app.session.rollback()
            raise erro

    def deletar_album_veiculo(self, id_album_veiculo: int):
        try:
            album_veiculo = (
                app.session.query(AlbumVeiculoModel)
                .filter_by(id_album_veiculo=id_album_veiculo)
                .first()
            )
            app.session.delete(album_veiculo)
            app.session.commit()
        except SQLAlchemyError as erro:
            app.session.rollback()
            raise erro
