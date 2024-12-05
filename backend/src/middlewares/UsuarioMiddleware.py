from functools import wraps
from flask import request, jsonify
from src.controllers.UsuarioController import UsuarioController

class UsuarioMiddleware:
    
    @staticmethod
    def verificar_email(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            email = request.json.get("email")
            usuario = UsuarioController.verificar_email(email)
            if usuario:
                return jsonify({"mensagem":"Tente com outras credenciais"}), 400
            return f(*args, **kwargs)
        return wrapper
    
    def verificar_documentos(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            cpf = request.json.get("cpf")
            rg = request.json.get("rg")
            
            documento = UsuarioController.verificar_documentos(cpf, rg)
            if documento:
                return jsonify({"mensagem":"Documento inválido."}), 400
            return f(*args, **kwargs)
        return wrapper