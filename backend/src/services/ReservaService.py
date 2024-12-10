from flask import current_app as app
from src.models import (
    ReservaModel,
    VeiculoModel,
    VeiculoReservaModel,
    UsuarioModel,
    UsuarioReservaModel,
)
from sqlalchemy.exc import SQLAlchemyError


class ReservaService:

    def criar_reserva(self, dados: dict):
        try:
            nova_reserva = ReservaModel(
                data_devolucao=dados.get("data_devolucao"),
                data_locacao=dados.get("data_locacao"),
                fk_id_seguro=dados.get("fk_id_seguro"),
                preco_total=dados.get("preco_total"),
                status=dados.get("status"),
            )
            app.db.session.add(nova_reserva)
            app.db.session.commit()
        except SQLAlchemyError as erro:
            app.db.session.rollback()
            raise erro

    def buscar_todas_reservas(self):
        try:
            reservas = (
                app.session.query(ReservaModel, VeiculoModel, UsuarioModel)
                .join(
                    VeiculoReservaModel,
                    ReservaModel.id == VeiculoReservaModel.fk_id_reserva,
                )
                .join(
                    VeiculoModel, VeiculoReservaModel.fk_id_veiculo == VeiculoModel.id
                )
                .join(
                    UsuarioReservaModel,
                    ReservaModel.id == UsuarioReservaModel.fk_id_reserva,
                )
                .join(
                    UsuarioModel, UsuarioReservaModel.fk_id_usuario == UsuarioModel.id
                )
                .group_by(ReservaModel.id)
                .all()
            )
            return reservas
        except SQLAlchemyError as erro:
            raise erro

    def buscar_reservas_do_usuario(self, id_usuario: int):
        try:
            reservas = (
                app.session.query(ReservaModel, VeiculoModel)
                .join(
                    VeiculoReservaModel,
                    ReservaModel.id == VeiculoReservaModel.fk_id_reserva,
                )
                .join(
                    VeiculoModel, VeiculoReservaModel.fk_id_veiculo == VeiculoModel.id
                )
                .filter(ReservaModel.fk_id_usuario == id_usuario)
                .all()
            )
            return reservas
        except SQLAlchemyError as erro:
            raise erro

    def buscar_reserva_por_id(self, id_reserva: int):
        try:
            reserva = (
                app.session.query(ReservaModel, VeiculoModel, UsuarioModel)
                .join(
                    VeiculoReservaModel,
                    ReservaModel.id == VeiculoReservaModel.fk_id_reserva,
                )
                .join(
                    VeiculoModel, VeiculoReservaModel.fk_id_veiculo == VeiculoModel.id
                )
                .join(
                    UsuarioReservaModel,
                    ReservaModel.id == UsuarioReservaModel.fk_id_reserva,
                )
                .join(
                    UsuarioModel, UsuarioReservaModel.fk_id_usuario == UsuarioModel.id
                )
                .filter(ReservaModel.id == id_reserva)
                .first()
            )
            return reserva
        except SQLAlchemyError as erro:
            raise erro

    def atualizar_reserva(self, id_reserva: int, dados: dict):
        try:
            reserva = (
                app.session.query(ReservaModel)
                .filter(ReservaModel.id_reserva == id_reserva)
                .first()
            )
            reserva.data_devolucao = dados.get("data_devolucao")
            reserva.data_locacao = dados.get("data_locacao")
            reserva.fk_id_seguro = dados.get("fk_id_seguro")
            reserva.preco_total = dados.get("preco_total")
            reserva.status = dados.get("status")
            app.session.commit()
            
            return reserva

        except SQLAlchemyError as erro:
            app.session.rollback()
            raise erro
    
    def deletar_reserva(self, id_reserva: int):
        try:
            reserva = (
                app.session.query(ReservaModel)
                .filter(ReservaModel.id_reserva == id_reserva)
                .first()
            )
            app.session.delete(reserva)
            app.session.commit()
        except SQLAlchemyError as erro:
            app.session.rollback()
            raise erro
