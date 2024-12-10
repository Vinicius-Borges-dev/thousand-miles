from flask import request, jsonify
from src.controllers.MarcaController import MarcaController
from functools import wraps

class AuthMarcaMiddleware:
    
    @staticmethod
    def verificar_existencia_marca(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            marca = request.form.get("nome_marca")
            verificacao_marca = MarcaController().buscar_marca_por_nome(marca)
            if verificacao_marca[1]==200:
                return jsonify({"status": "erro", "mensagem": "Marca já cadastrada."}), 409
            return f(*args, **kwargs)
        return wrapper