from src.controllers.CambioController import CambioController
from flask import request, jsonify
from functools import wraps


class AuthCambioMiddleware:

    @staticmethod
    def verificar_existencia_cambio(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            cambio = request.form.get("nome_cambio")
            verificacao_cambio = CambioController().buscar_cambio_por_nome(cambio)
            if verificacao_cambio[1] == 200:
                return (
                    jsonify({"status": "erro", "mensagem": "Cambio já cadastrado."}),
                    409,
                )
            return f(*args, **kwargs)

        return wrapper
