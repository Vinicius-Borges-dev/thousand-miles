from flask import current_app as app
from sqlalchemy.exc import SQLAlchemyError
from src.models import EnderecoModel

class EnderecoService:
    
    def criar_endereco(self, dados:dict):
        try:
            novo_endereco = EnderecoModel(
                rua=dados.get('rua'),
                numero=dados.get('numero'),
                fk_id_bairro=dados.get('id_bairro')
            )
            app.session.add(novo_endereco)
            app.session.commit()
            
            return novo_endereco
        except SQLAlchemyError as erro:
            app.session.rollback()
            return erro
    
    def capturar_endereco_por_id(self, id_endereco:int):
        try:
            endereco = app.session.query(EnderecoModel).filter_by(id_endereco=id_endereco).first()
            return endereco
        except SQLAlchemyError as erro:
            app.session.rollback()
            return erro
    
    def capturar_endereco_por_rua(self, rua:str):
        try:
            endereco = app.session.query(EnderecoModel).filter_by(rua=rua).first()
            return endereco
        except SQLAlchemyError as erro:
            app.session.rollback()
            return erro
    
    def capturar_endereco_por_rua_e_numero(self, rua:str, numero:int):
        try:
            endereco = app.session.query(EnderecoModel).filter(EnderecoModel.rua==rua, EnderecoModel.numero==numero).first()
            return endereco
        except SQLAlchemyError as erro:
            app.session.rollback()
            return erro
        
    def atualizar_endereco(self, id_endereco:int, dados:dict):
        try:
            endereco = app.session.query(EnderecoModel).filter_by(id_endereco=id_endereco).first()
            endereco.rua = dados.get('rua')
            endereco.numero = dados.get('numero')
            endereco.fk_id_bairro = dados.get('id_bairro')
            app.session.commit()
            return endereco
        except SQLAlchemyError as erro:
            app.session.rollback()
            return erro
    
    def deletar_endereco(self, id_endereco:int):
        try:
            endereco = app.session.query(EnderecoModel).filter_by(id_endereco=id_endereco).first()
            app.session.delete(endereco)
            app.session.commit()
            return True
        except SQLAlchemyError as erro:
            app.session.rollback()
            return erro