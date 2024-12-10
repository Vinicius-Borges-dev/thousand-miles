from src.models import (
    VeiculoModel,
    ModeloModel,
    CambioModel,
    CategoriaModel,
    CombustivelModel,
)
from sqlalchemy.exc import SQLAlchemyError
from flask import current_app as app
from sqlalchemy.sql.expression import func


class VeiculoService:

    def criar_veículo(self, dados: dict):
        try:
            veiculo = VeiculoModel(
                ano_fabricacao=dados.get("ano_fabricacao"),
                assentos=dados.get("assentos"),
                cor=dados.get("cor"),
                disponivel=dados.get("disponivel"),
                placa=dados.get("placa"),
                preco_por_dia=dados.get("preco_por_dia"),
                id_album_veiculo=dados.get("id_album_veiculo"),
                id_categoria=dados.get("id_categoria"),
                id_cambio=dados.get("id_cambio"),
                id_combustivel=dados.get("id_combustivel"),
                id_modelo=dados.get("id_modelo"),
            )
            app.session.add(veiculo)
            app.session.commit()

            return veiculo
        except SQLAlchemyError as erro:
            app.session.rollback()
            raise erro

    def buscar_veiculo_por_placa(self, placa: str):
        try:
            veiculo = app.session.query(VeiculoModel).filter_by(placa=placa).first()
            return veiculo
        except SQLAlchemyError as erro:
            raise erro

    def buscar_veiculo_por_modelo(self, modelo: str):
        try:
            veiculo = (
                app.session.query(VeiculoModel)
                .join(ModeloModel)
                .filter(ModeloModel.nome_modelo == modelo)
                .first()
            )

            return veiculo
        except SQLAlchemyError as erro:
            raise erro

    def buscar_veiculo_por_id(self, id_veiculo: int):
        try:
            veiculo = (
                app.session.query(VeiculoModel).filter_by(id_veiculo=id_veiculo).first()
            )
            return veiculo
        except SQLAlchemyError as erro:
            raise erro

    def buscar_todos_veiculos(self):
        try:
            veiculos = app.session.query(VeiculoModel).all()
            return veiculos
        except SQLAlchemyError as erro:
            raise erro

    def buscar_veiculo_aleatorio_disponivel(self, nome_modelo: str):
        try:
            veiculo = (
                app.session.query(VeiculoModel)
                .join(ModeloModel, VeiculoModel.fk_id_modelo == ModeloModel.id_modelo)
                .filter(VeiculoModel.disponivel == 1, ModeloModel.nome_modelo == nome_modelo)
                .order_by(func.random())
                .first()
            )
            return veiculo
        except SQLAlchemyError as erro:
            raise erro

    def atualizar_veiculo(self, id_veiculo: int, dados: dict):
        try:
            veiculo = self.buscar_veiculo_por_id(id_veiculo)
            veiculo.ano_fabricacao = dados.get("ano_fabricacao")
            veiculo.assentos = dados.get("assentos")
            veiculo.cor = dados.get("cor")
            veiculo.disponivel = dados.get("disponivel")
            veiculo.placa = dados.get("placa")
            veiculo.preco_por_dia = dados.get("preco_por_dia")
            veiculo.id_album_veiculo = dados.get("id_album_veiculo")
            veiculo.id_categoria = dados.get("id_categoria")
            veiculo.id_cambio = dados.get("id_cambio")
            veiculo.id_combustivel = dados.get("id_combustivel")
            veiculo.id_modelo = dados.get("id_modelo")

            app.session.commit()

            return veiculo
        except SQLAlchemyError as erro:
            app.session.rollback()
            raise erro

    def buscar_todos_veiculos_por_modelo(self, modelo: str):
        try:
            veiculos = (
                app.session.query(VeiculoModel)
                .join(ModeloModel)
                .filter(ModeloModel.nome_modelo == modelo)
                .all()
            )
            return veiculos
        except SQLAlchemyError as erro:
            raise erro

    def buscar_todos_veiculos_por_categoria(self, categoria: str):
        try:
            veiculos = (
                app.session.query(VeiculoModel)
                .join(CategoriaModel)
                .filter(CategoriaModel.nome_categoria == categoria)
                .all()
            )
            return veiculos
        except SQLAlchemyError as erro:
            raise erro

    def buscar_todos_veiculos_por_cambio(self, cambio: str):
        try:
            veiculos = (
                app.session.query(VeiculoModel)
                .join(CambioModel)
                .filter(CambioModel.tipo_cambio == cambio)
                .all()
            )
            return veiculos
        except SQLAlchemyError as erro:
            raise erro

    def buscar_todos_veiculos_por_combustivel(self, combustivel: str):
        try:
            veiculos = (
                app.session.query(VeiculoModel)
                .join(CombustivelModel)
                .filter(CombustivelModel.tipo_combustivel == combustivel)
                .all()
            )
            return veiculos
        except SQLAlchemyError as erro:
            raise erro

    def alterar_disponibilidade_veiculo(self, id_veiculo: int, disponibilidade: int):
        try:
            veiculo = self.buscar_veiculo_por_id(id_veiculo)
            veiculo.disponivel = disponibilidade
            app.session.commit()
            return veiculo
        except SQLAlchemyError as erro:
            app.session.rollback()
            raise erro

    def deletar_veiculo(self, id_veiculo: int):
        try:
            veiculo = self.buscar_veiculo_por_id(id_veiculo)
            app.session.delete(veiculo)
            app.session.commit()
        except SQLAlchemyError as erro:
            app.session.rollback()
            raise erro

    def buscar_veiculos_por_modelo_disponiveis(self):
        try:
            veiculos = (
                app.session.query(VeiculoModel)
                .join(ModeloModel, VeiculoModel.fk_id_modelo == ModeloModel.id_modelo)
                .filter(VeiculoModel.disponivel == 1)
                .group_by(ModeloModel.id_modelo)
                .having(func.count(VeiculoModel.id_veiculo) > 0)
            ).all()
            return veiculos
        except SQLAlchemyError as erro:
            raise erro
