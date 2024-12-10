from flask import request, jsonify
from src.controllers.CombustivelController import CombustivelController
from functools import wraps

class AuthCombustivelMiddleware:
    
    @staticmethod
    def verificar_existencia_combustivel(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            combustivel = request.form.get("tipo_combustivel")
            verificacao_combustivel = CombustivelController().buscar_combustivel_por_nome(combustivel)
            if verificacao_combustivel[1]==200:
                return jsonify({"status": "erro", "mensagem": "Combustível já cadastrado."}), 409
            return f(*args, **kwargs)
        return wrapper
