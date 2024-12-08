from functools import wraps
from flask import request, jsonify
from src.controllers.UsuarioController import UsuarioController
from src.services.UsuarioService import UsuarioService
import jwt
from os import environ

class UsuarioMiddleware:

    @staticmethod
    def verificar_email(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            email = request.json.get("email")
            usuario = UsuarioController.verificar_email(email)
            if usuario:
                return jsonify({"mensagem": "Tente com outras credenciais"}), 400
            return f(*args, **kwargs)
        return wrapper

    @staticmethod
    def verificar_documentos(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            cpf = request.json.get("cpf")
            rg = request.json.get("rg")
            documento = UsuarioController.verificar_documentos(cpf, rg)
            if documento:
                return jsonify({"mensagem": "Documento inválido."}), 400
            return f(*args, **kwargs)
        return wrapper

    @staticmethod
    def validar_existencia_token(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            token = request.headers.get("Authorization")
            if not token:
                return jsonify({"mensagem": "Autorização não está presente."}), 400
            return f(*args, **kwargs)
        return wrapper

    @staticmethod
    def validar_dados_token(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            if not UsuarioMiddleware._extrair_e_verificar_token():
                return jsonify({"status": "erro", "mensagem": "Token inválido ou expirado."}), 401
            return f(*args, **kwargs)
        return wrapper

    @staticmethod
    def capturar_permissao_de_funcionario(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            dados_token = UsuarioMiddleware._extrair_e_verificar_token()
            if not dados_token:
                return jsonify({"mensagem": "Acesso negado."}), 401
            if dados_token.get("nivel_acesso") != "admin":
                return jsonify({"mensagem": "Você não tem permissão para realizar essa operação."}), 401
            return f(*args, **kwargs)
        return wrapper

    @staticmethod
    def _extrair_e_verificar_token():
        token = request.headers.get("Authorization")
        if not token or not token.startswith("Bearer "):
            return None
        token = token[7:]
        chave = environ.get("SECRET_KEY")
        try:
            dados_token = jwt.decode(token, chave, algorithms=["HS256"])
            if not dados_token.get("usuario") or not dados_token.get("nivel_acesso"):
                return None
            if not UsuarioService().capturar_informacoes_usuario(dados_token.get("usuario")):
                return None
            return dados_token
        except (jwt.ExpiredSignatureError, jwt.InvalidTokenError):
            return None
