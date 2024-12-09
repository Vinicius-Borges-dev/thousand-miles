from src.models import CategoriaModel
from sqlalchemy.exc import SQLAlchemyError
from flask import current_app as app


class CategoriaService:

    def criar_categoria(self, dados: dict):
        try:
            categoria = CategoriaModel(nome_categoria=dados.get("nome_categoria"))
            app.session.add(categoria)
            app.session.commit()

            return categoria
        except SQLAlchemyError as erro:
            app.session.rollback()
            raise erro

    def buscar_todas_categorias(self):
        try:
            categorias = app.session.query(CategoriaModel).all()
            return categorias
        except SQLAlchemyError as erro:
            raise erro

    def buscar_categoria_por_id(self, id_categoria: int):
        try:
            categoria = (
                app.session.query(CategoriaModel)
                .filter_by(id_categoria=id_categoria)
                .first()
            )
            return categoria
        except SQLAlchemyError as erro:
            raise erro

    def buscar_categoria_por_nome(self, nome_categoria: str):
        try:
            categoria = (
                app.session.query(CategoriaModel)
                .filter_by(nome_categoria=nome_categoria)
                .first()
            )
            return categoria
        except SQLAlchemyError as erro:
            raise erro

    def atualizar_categoria(self, id_categoria: int, dados: dict):
        try:
            categoria = (
                app.session.query(CategoriaModel)
                .filter_by(id_categoria=id_categoria)
                .first()
            )
            categoria.nome_categoria = dados.get("nome_categoria")
            app.session.commit()

            return categoria
        except SQLAlchemyError as erro:
            app.session.rollback()
            raise erro

    def deletar_categoria(self, id_categoria: int):
        try:
            categoria = (
                app.session.query(CategoriaModel)
                .filter_by(id_categoria=id_categoria)
                .first()
            )
            app.session.delete(categoria)
            app.session.commit()
        except SQLAlchemyError as erro:
            app.session.rollback()
            raise erro
    
    def buscar_por_nome_semelhante(self, nome_categoria: str):
        try:
            categorias = (
                app.session.query(CategoriaModel)
                .filter(CategoriaModel.nome_categoria.like(f"%{nome_categoria}%"))
                .all()
            )
            return categorias
        except SQLAlchemyError as erro:
            raise erro
