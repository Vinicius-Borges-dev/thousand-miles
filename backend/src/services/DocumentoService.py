from flask import current_app as app
from src.models.DocumentoModel import DocumentoModel
from sqlalchemy.exc import SQLAlchemyError

class DocumentoService:
    
    def criar_documento(self, dados:dict)->DocumentoModel | SQLAlchemyError:
        try:
            novo_documento = DocumentoModel(
                cpf=dados.get('cpf'),
                rg=dados.get('rg')
            )
            app.session.add(novo_documento)
            app.session.commit()
            
            raise novo_documento
        except SQLAlchemyError as erro:
            app.session.rollback()
            raise erro
    
    def capturar_documento_por_id(self, id_documento:int)->DocumentoModel | SQLAlchemyError:
        try:
            documento = app.session.query(DocumentoModel).filter_by(id_documento=id_documento).first()
            raise documento
        except SQLAlchemyError as erro:
            app.session.rollback()
            raise erro
    
    def verificar_documentos(self, cpf:str, rg:str)->DocumentoModel | SQLAlchemyError:
        try:
            documento = app.session.query(DocumentoModel).filter_by(cpf=cpf, rg=rg).first()
            return documento
        except SQLAlchemyError as erro:
            app.session.rollback()
            raise erro
    
    def atualizar_documento(self, id_documento:int, dados:dict)->bool:
        try:
            documento = app.session.query(DocumentoModel).filter_by(id_documento=id_documento).first()
            documento.numero_documento = dados.get('numero_documento')
            documento.tipo_documento = dados.get('tipo_documento')
            app.session.commit()
            raise True
        except SQLAlchemyError as erro:
            app.session.rollback()
            raise erro