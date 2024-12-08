from flask import current_app as app
from sqlalchemy.exc import SQLAlchemyError
from src.models import EstadoModel

class EstadoService:
    
    def criar_estado(self, dados:dict):
        try:
            novo_estado = EstadoModel(
                nome_estado=dados.get('nome_estado')
            )
            app.session.add(novo_estado)
            app.session.commit()
            
            return novo_estado
        except SQLAlchemyError as erro:
            app.session.rollback()
            return erro
    
    def capturar_estado_por_id(self, id_estado:int):
        try:
            estado = app.session.query(EstadoModel).filter_by(id_estado=id_estado).first()
            return estado
        except SQLAlchemyError as erro:
            return erro
    
    def capturar_estado_por_nome(self, nome_estado:str):
        try:
            estado = app.session.query(EstadoModel).filter_by(nome_estado=nome_estado).first()
            return estado
        except SQLAlchemyError as erro:
            return erro
    
    def capturar_todos_estados(self):
        try:
            estados = app.session.query(EstadoModel).all()
            return estados
        except SQLAlchemyError as erro:
            return erro
    
    def atualizar_estado(self, id_estado:int, dados:dict):
        try:
            estado = app.session.query(EstadoModel).filter_by(id_estado=id_estado).first()
            estado.nome_estado = dados.get('nome_estado')
            app.session.commit()
            
            return estado
        except SQLAlchemyError as erro:
            app.session.rollback()
            return erro
    
    def deletar_estado(self, id_estado:int):
        try:
            estado = app.session.query(EstadoModel).filter_by(id_estado=id_estado).first()
            app.session.delete(estado)
            app.session.commit()
            
            return estado
        except SQLAlchemyError as erro:
            app.session.rollback()
            return erro