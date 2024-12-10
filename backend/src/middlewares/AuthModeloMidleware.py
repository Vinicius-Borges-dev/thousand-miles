from flask import request, jsonify, Response
from src.controllers.ModeloController import ModeloController
from functools import wraps

class AuthModeloMiddleware:
    
    @staticmethod
    def verificar_existencia_modelo(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            modelo = request.form.get("nome_modelo")
            verificaca_modelo = ModeloController().buscar_por_nome(modelo)
            if verificaca_modelo[1] == 200:
                return jsonify({"status": "erro", "mensagem": "Modelo já cadastrado."}), 409
            return f(*args, **kwargs)
        return wrapper