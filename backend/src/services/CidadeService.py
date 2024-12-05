from flask import current_app as app
from sqlalchemy.exc import SQLAlchemyError
from src.models import CidadeModel

class CidadeService:
    
    def criar_cidade(self, dados:dict):
        try:
            nova_cidade = CidadeModel(
                nome_cidade=dados.get('nome_cidade'),
                id_estado=dados.get('id_estado')
            )
            app.session.add(nova_cidade)
            app.session.commit()
            
            return nova_cidade
        except SQLAlchemyError as erro:
            app.session.rollback()
            return erro
    
    def capturar_cidade_por_id(self, id_cidade:int):
        try:
            cidade = app.session.query(CidadeModel).filter_by(id_cidade=id_cidade).first()
            return cidade
        except SQLAlchemyError as erro:
            app.session.rollback()
            return erro
    
    def capturar_cidade_por_nome(self, nome_cidade:str):
        try:
            cidade = app.session.query(CidadeModel).filter_by(nome_cidade=nome_cidade).first()
            return cidade
        except SQLAlchemyError as erro:
            app.session.rollback()
            return erro
    
    def capturar_cidades(self):
        try:
            cidades = app.session.query(CidadeModel).all()
            return cidades
        except SQLAlchemyError as erro:
            app.session.rollback()
            return erro
    
    def atualizar_cidade(self, id_cidade:int, dados:dict):
        try:
            cidade = app.session.query(CidadeModel).filter_by(id_cidade=id_cidade).first()
            cidade.nome_cidade = dados.get('nome_cidade')
            cidade.id_estado = dados.get('id_estado')
            app.session.commit()
            return cidade
        except SQLAlchemyError as erro:
            app.session.rollback()
            return erro
    
    def deletar_cidade(self, id_cidade:int):
        try:
            cidade = app.session.query(CidadeModel).filter_by(id_cidade=id_cidade).first()
            app.session.delete(cidade)
            app.session.commit()
            return cidade
        except SQLAlchemyError as erro:
            app.session.rollback()
            return erro