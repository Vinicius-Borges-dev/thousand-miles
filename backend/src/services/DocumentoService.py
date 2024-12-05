from flask import current_app as app
from src.models.DocumentoModel import DocumentoModel
from sqlalchemy.exc import SQLAlchemyError

class DocumentoService:
    
    def criar_documento(self, dados:dict)->DocumentoModel:
        try:
            novo_documento = DocumentoModel(
                numero_documento=dados.get('numero_documento'),
                tipo_documento=dados.get('tipo_documento'),
            )
            app.session.add(novo_documento)
            app.session.commit()
            return novo_documento
        except SQLAlchemyError as erro:
            app.session.rollback()
            return erro
    
    def capturar_documento(self, id_documento:int)->DocumentoModel:
        try:
            documento = app.session.query(DocumentoModel).filter_by(id_documento=id_documento).first()
            return documento
        except SQLAlchemyError as erro:
            app.session.rollback()
            return erro
    
    def atualizar_documento(self, id_documento:int, dados:dict)->bool:
        try:
            documento = app.session.query(DocumentoModel).filter_by(id_documento=id_documento).first()
            documento.numero_documento = dados.get('numero_documento')
            documento.tipo_documento = dados.get('tipo_documento')
            app.session.commit()
            return True
        except SQLAlchemyError as erro:
            app.session.rollback()
            return erro