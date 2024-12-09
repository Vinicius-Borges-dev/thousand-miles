from flask import request, jsonify
from src.services.CategoriaService import CategoriaService


class CategoriaController:

    def criar_categoria(self):
        dados = request.json
        try:
            categoria_service = CategoriaService()
            categoria = categoria_service.criar_categoria(
                {"nome_categoria": dados.get("nome_categoria")}
            )
            return (
                jsonify(
                    {
                        "status": "ok",
                        "mensagem": "Categoria criada com sucesso",
                    }
                ),
                201,
            )
        except Exception as erro:
            return (
                jsonify(
                    {
                        "status": "erro",
                        "mensagem": "Erro ao criar categoria",
                        "erro": str(erro),
                    }
                ),
                500,
            )

    def buscar_todas_categorias(self):
        try:
            categoria = CategoriaService().buscar_todas_categorias()
            if categoria:
                return (
                    jsonify(
                        {
                            "status": "ok",
                            "mensagem": "Categorias encontradas",
                            "dados": categoria,
                        }
                    ),
                    200,
                )
            else:
                return (
                    jsonify(
                        {
                            "status": "erro",
                            "mensagem": "Nenhuma categoria encontrada",
                        }
                    ),
                    404,
                )
        except Exception as erro:
            return (
                jsonify(
                    {
                        "status": "erro",
                        "mensagem": "Erro ao buscar categorias",
                        "erro": str(erro),
                    }
                ),
                500,
            )

    def buscar_categoria_por_id(self, id_categoria: int):
        try:
            categoria = CategoriaService().buscar_categoria_por_id(id_categoria)
            if categoria:
                return (
                    jsonify(
                        {
                            "status": "ok",
                            "mensagem": "Categoria encontrada",
                            "dados": categoria,
                        }
                    ),
                    200,
                )
            else:
                return (
                    jsonify(
                        {
                            "status": "erro",
                            "mensagem": "Categoria não encontrada",
                        }
                    ),
                    404,
                )
        except Exception as erro:
            return (
                jsonify(
                    {
                        "status": "erro",
                        "mensagem": "Erro ao buscar categoria",
                        "erro": str(erro),
                    }
                ),
                500,
            )

    def buscar_categoria_por_nome(self, nome_categoria: str):
        try:
            categoria = CategoriaService().buscar_categoria_por_nome(nome_categoria)
            if categoria:
                return (
                    jsonify(
                        {
                            "status": "ok",
                            "mensagem": "Categoria encontrada",
                            "dados": categoria,
                        }
                    ),
                    200,
                )
            else:
                return (
                    jsonify({"status": "erro", "mensagem": "Categoria não encontrada"}),
                    404,
                )
        except Exception as erro:
            return (
                jsonify(
                    {
                        "status": "erro",
                        "mensagem": "Erro ao buscar categoria",
                        "erro": str(erro),
                    }
                ),
                500,
            )

    def atualizar_categoria(self, id_categoria: int):
        nome_categoria = request.json.get("nome_categoria")
        try:
            categoria_service = CategoriaService()
            categoria = categoria_service.atualizar_categoria(
                id_categoria, {"nome_categoria": nome_categoria}
            )
            return (
                jsonify(
                    {
                        "status": "ok",
                        "mensagem": "Categoria atualizada com sucesso",
                    }
                ),
                200,
            )
        except Exception as erro:
            return (
                jsonify(
                    {
                        "status": "erro",
                        "mensagem": "Erro ao atualizar categoria",
                        "erro": str(erro),
                    }
                ),
                500,
            )

    def deletar_categoria(self, id_categoria: int):
        try:
            categoria_service = CategoriaService()
            categoria_service.deletar_categoria(id_categoria)
            return jsonify({"mensagem": "Categoria deletada com sucesso"}), 200
        except Exception as erro:
            return (
                jsonify(
                    {
                        "status": "erro",
                        "mensagem": "Erro ao deletar categoria",
                        "erro": str(erro),
                    }
                ),
                500,
            )
