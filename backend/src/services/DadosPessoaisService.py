from flask import current_app as app
from sqlalchemy.exc import SQLAlchemyError
from src.models import DadosPessoaisModel

class DadosPessoaisService:
    
    def criar_dados_pessoais(self, dados: dict):
        try:
            novos_dados_pessoais = DadosPessoaisModel(
                nome=dados.get("nome"),
                sobrenome=dados.get("sobrenome"),
                fk_id_documento=dados.get("id_documento"),
                data_nascimento=dados.get("data_nascimento"),
            )

            app.session.add(novos_dados_pessoais)
            app.session.commit()

            return novos_dados_pessoais
        except SQLAlchemyError as erro:
            app.session.rollback()
            return erro
    
    def editar_dados_pessoais(self, id_dados_pessoais: int, dados: dict):
        try:
            dados_pessoais = app.session.query(DadosPessoaisModel).filter_by(id_dados_pessoais=id_dados_pessoais).first()

            dados_pessoais.nome = dados.get("nome")
            dados_pessoais.sobrenome = dados.get("sobrenome")
            dados_pessoais.fk_id_documento = dados.get("id_documento")

            app.session.commit()

            return dados_pessoais
        except SQLAlchemyError as erro:
            app.session.rollback()
            return erro
    
    def capturar_informacao_dados_pessoais(self, id_dados_pessoais: int):
        try:
            dados_pessoais = app.session.query(DadosPessoaisModel).filter_by(id_dados_pessoais=id_dados_pessoais).first()
            return dados_pessoais
        except SQLAlchemyError as erro:
            app.session.rollback()
            return erro
    
    def deletar_dados_pessoais(self, id_dados_pessoais: int):
        try:
            dados_pessoais = app.session.query(DadosPessoaisModel).filter_by(id_dados_pessoais=id_dados_pessoais).first()
            
            app.session.delete(dados_pessoais)
            app.session.commit()
            
            return True
        except SQLAlchemyError as erro:
            app.session.rollback()
            return erro