from src.services.ModeloService import ModeloService
from flask import request, jsonify


class ModeloController:

    def criar_modelo(self):
        try:
            nome_modelo = request.json.get("nome_modelo")
            id_marca = request.json.get("id_marca")
            modelo = ModeloService().criar_modelo(
                {"nome_modelo": nome_modelo, "id_marca": id_marca}
            )
            return (
                jsonify(
                    {
                        "status": "ok",
                        "mensagem": "Modelo cadastrado com sucesso",
                    }
                ),
                201,
            )
        except Exception as erro:
            return jsonify(
                {
                    "status": "erro",
                    "mensagem": "Erro ao cadastrar modelo",
                    "erro": str(erro),
                }
            )

    def buscar_por_id(self, id_modelo: int):
        try:
            modelo = ModeloService().buscar_modelo_por_id(id_modelo)
            if modelo:
                return jsonify(
                    {"status": "ok", "mensagem": "Modelo encontrado", "dados": modelo}
                )
            else:
                return (
                    jsonify({"status": "erro", "mensagem": "Modelo não encontrado"}),
                    404,
                )
        except Exception as erro:
            return (
                jsonify(
                    {
                        "status": "erro",
                        "mensagem": "Erro ao buscar modelo",
                        "erro": str(erro),
                    }
                ),
                500,
            )

    def buscar_por_nome(self):
        nome_modelo = request.json.get("nome_modelo")
        try:
            modelo = ModeloService().buscar_modelo_por_nome(nome_modelo)
            if modelo:
                return jsonify(
                    {"status": "ok", "mensagem": "Modelo encontrado", "dados": modelo}
                )
            else:
                return (
                    jsonify({"status": "erro", "mensagem": "Modelo não encontrado"}),
                    404,
                )
        except Exception as erro:
            return jsonify(
                {
                    "status": "erro",
                    "mensagem": "Erro ao buscar modelo",
                    "erro": str(erro),
                }
            )

    def editar_modelo(self, id_modelo: int):
        try:
            nome_modelo = request.json.get("nome_modelo")
            id_marca = request.json.get("id_marca")
            modelo = ModeloService().atualizar_modelo(
                id_modelo, {"nome_modelo": nome_modelo, "id_marca": id_marca}
            )
            return (
                jsonify(
                    {
                        "status": "ok",
                        "mensagem": "Modelo editado com sucesso",
                    }
                ),
                200,
            )
        except Exception as erro:
            return jsonify(
                {
                    "status": "erro",
                    "mensagem": "Erro ao editar modelo",
                    "erro": str(erro),
                }
            )

    def buscar_todos(self):
        try:
            modelos = ModeloService().buscar_todos_modelos()
            if modelos:
                lista = []
                for modelo in modelos:
                    lista.append(
                        {
                            "id_modelo": modelo.id_modelo,
                            "nome_modelo": modelo.nome_modelo,
                            "id_marca": modelo.id_marca,
                            "nome_marca": modelo.marca.nome_marca,
                        }
                    )
                return jsonify(
                    {
                        "status": "ok",
                        "mensagem": "Modelos encontrados",
                        "dados": lista,
                    }
                )
            else:
                return (
                    jsonify({"status": "erro", "mensagem": "Modelo não encontrado"}),
                    404,
                )
        except Exception as erro:
            return jsonify(
                {
                    "status": "erro",
                    "mensagem": "Erro ao buscar modelos",
                    "erro": str(erro),
                }
            )

    def excluir_modelo(self, id_modelo: int):
        try:
            ModeloService().deletar_modelo(id_modelo)
            return (
                jsonify(
                    {
                        "status": "ok",
                        "mensagem": "Modelo excluído com sucesso",
                    }
                ),
                200,
            )
        except Exception as erro:
            return jsonify(
                {
                    "status": "erro",
                    "mensagem": "Erro ao excluir modelo",
                    "erro": str(erro),
                }
            )

    def buscar_nome_semelhante(self, nome_modelo: str):
        try:
            modelos = ModeloService().buscar_modelo_por_nome(nome_modelo)
            if modelos:
                lista = []
                for modelo in modelos:
                    lista.append(
                        {
                            "id_modelo": modelo.id_modelo,
                            "nome_modelo": modelo.nome_modelo,
                            "id_marca": modelo.id_marca,
                            "nome_marca": modelo.marca.nome_marca,
                        }
                    )
                return jsonify(
                    {
                        "status": "ok",
                        "mensagem": "Modelos encontrados",
                        "dados": lista,
                    }
                )
            else:
                return (
                    jsonify({"status": "erro", "mensagem": "Modelo não encontrado"}),
                    404,
                )
        except Exception as erro:
            return jsonify(
                {
                    "status": "erro",
                    "mensagem": "Erro ao buscar modelos",
                    "erro": str(erro),
                }
            )
