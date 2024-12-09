from flask import request, jsonify
from src.services.CambioService import CambioService


class CambioController:

    def criar_cambio(self):
        nome_cambio = request.form.get("nome_cambio")
        try:
            cambio = CambioService().criar_cambio({"nome_cambio": nome_cambio})
            return (
                jsonify(
                    {
                        "status": "ok",
                        "mensagem": "Câmbio criado com sucesso",
                    }
                ),
                201,
            )
        except Exception as erro:
            return (
                jsonify(
                    {
                        "status": "erro",
                        "mensagem": "Erro ao criar câmbio",
                        "erro": str(erro),
                    }
                ),
                500,
            )

    def buscar_todos_cambios(self):
        try:
            cambios = CambioService().buscar_todos_cambios()
            if cambios:
                return jsonify(
                    {
                        "status": "ok",
                        "mensagem": "Câmbios encontrados",
                        "dados": [cambio.to_dict() for cambio in cambios],
                    }
                )
            else:
                return (
                    jsonify({"status": "erro", "mensagem": "Nenhum câmbio encontrado"}),
                    404,
                )
        except Exception as erro:
            return (
                jsonify(
                    {
                        "status": "erro",
                        "mensagem": "Erro ao buscar câmbios",
                        "erro": str(erro),
                    }
                ),
                500,
            )

    def buscar_cambio_por_id(self, id_cambio: int):
        try:
            cambio = CambioService().buscar_cambio_por_id(id_cambio)
            if cambio:
                return jsonify(
                    {
                        "status": "ok",
                        "mensagem": "Câmbio encontrado",
                        "dados": cambio.to_dict(),
                    }
                )
            else:
                return (
                    jsonify({"status": "erro", "mensagem": "Câmbio não encontrado"}),
                    404,
                )
        except Exception as erro:
            return (
                jsonify(
                    {
                        "status": "erro",
                        "mensagem": "Erro ao buscar câmbio",
                        "erro": str(erro),
                    }
                ),
                500,
            )

    def buscar_cambio_por_nome(self, nome_cambio: str):
        try:
            cambio = CambioService().buscar_cambio_por_nome(nome_cambio)
            if cambio:
                return jsonify(
                    {
                        "status": "ok",
                        "mensagem": "Câmbio encontrado",
                        "dados": cambio.to_dict(),
                    }
                )
            else:
                return (
                    jsonify({"status": "erro", "mensagem": "Câmbio não encontrado"}),
                    404,
                )
        except Exception as erro:
            return (
                jsonify(
                    {
                        "status": "erro",
                        "mensagem": "Erro ao buscar câmbio",
                        "erro": str(erro),
                    }
                ),
                500,
            )

    def atualizar_cambio(self, id_cambio: int):
        nome_cambio = request.form.get("nome_cambio")
        try:
            cambio = CambioService().atualizar_cambio(
                id_cambio, {"tipo_cambio": nome_cambio}
            )
            return (
                jsonify(
                    {
                        "status": "ok",
                        "mensagem": "Câmbio atualizado com sucesso",
                    }
                ),
                200,
            )
        except Exception as erro:
            return (
                jsonify(
                    {
                        "status": "erro",
                        "mensagem": "Erro ao atualizar câmbio",
                        "erro": str(erro),
                    }
                ),
                500,
            )

    def deletar_cambio(self, id_cambio: int):
        try:
            CambioService().deletar_cambio(id_cambio)
            return jsonify({"mensagem": "Câmbio deletado com sucesso"}), 200
        except Exception as erro:
            return (
                jsonify({"mensagem": "Erro ao deletar câmbio", "erro": str(erro)}),
                500,
            )

    def buscar_por_nome_semelhante(self, nome: str):
        try:
            cambios = CambioService().buscar_cambio_por_nome_semelhante(nome)
            if cambios:
                return jsonify(
                    {
                        "status": "ok",
                        "mensagem": "Câmbios encontrados",
                        "dados": [cambio.to_dict() for cambio in cambios],
                    }
                )
            else:
                return (
                    jsonify({"status": "erro", "mensagem": "Nenhum câmbio encontrado"}),
                    404,
                )
        except Exception as erro:
            return (
                jsonify(
                    {
                        "status": "erro",
                        "mensagem": "Erro ao buscar câmbios",
                        "erro": str(erro),
                    }
                ),
                500,
            )
