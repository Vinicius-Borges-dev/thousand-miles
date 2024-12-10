from flask import request, jsonify
from src.controllers.CategoriaController import CategoriaController
from functools import wraps


class AuthCategoriaMiddleware:

    @staticmethod
    def verificar_existencia_categoria(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            categoria = request.form.get("nome_categoria")
            verificacao_categoria = CategoriaController().buscar_categoria_por_nome(
                categoria
            )
            if verificacao_categoria[1] == 200:
                return (
                    jsonify({"status": "erro", "mensagem": "Categoria já cadastrada."}),
                    409,
                )
            return f(*args, **kwargs)

        return wrapper
