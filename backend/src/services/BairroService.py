from flask import current_app as app
from sqlalchemy.exc import SQLAlchemyError
from src.models import BairroModel

class BairroService:
    
    def criar_bairro(self, dados:dict):
        try:
            novo_bairro = BairroModel(
                nome_bairro=dados.get('nome_bairro'),
                fk_id_cidade=dados.get('id_cidade')
            )
            app.session.add(novo_bairro)
            app.session.commit()
            
            return novo_bairro
        except SQLAlchemyError as erro:
            app.session.rollback()
            return erro
    
    def capturar_bairro_por_id(self, id_bairro:int):
        try:
            bairro = app.session.query(BairroModel).filter_by(id_bairro=id_bairro).first()
            return bairro
        except SQLAlchemyError as erro:
            app.session.rollback()
            return erro
    
    def capturar_bairro_por_nome(self, nome_bairro:str):
        try:
            bairro = app.session.query(BairroModel).filter_by(nome_bairro=nome_bairro).first()
            return bairro
        except SQLAlchemyError as erro:
            app.session.rollback()
            return erro
    
    def capturar_bairros(self):
        try:
            bairros = app.session.query(BairroModel).all()
            return bairros
        except SQLAlchemyError as erro:
            app.session.rollback()
            return erro
    
    def atualizar_bairro(self, id_bairro:int, dados:dict):
        try:
            bairro = app.session.query(BairroModel).filter_by(id_bairro=id_bairro).first()
            bairro.nome_bairro = dados.get('nome_bairro')
            bairro.fk_id_cidade = dados.get('fk_id_cidade')
            app.session.commit()
            return bairro
        except SQLAlchemyError as erro:
            app.session.rollback()
            return erro
    
    def deletar_bairro(self, id_bairro:int):
        try:
            bairro = app.session.query(BairroModel).filter_by(id_bairro=id_bairro).first()
            app.session.delete(bairro)
            app.session.commit()
            return bairro
        except SQLAlchemyError as erro:
            app.session.rollback()
            return erro