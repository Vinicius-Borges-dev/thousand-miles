from flask import request, jsonify
from src.services.CombustivelService import CombustivelService
import traceback

class CombustivelController:

    def criar_combustivel(self):
        tipo_combustivel = request.form.get("tipo_combustivel")
        try:
            combustivel = CombustivelService().criar_combustivel(
                {"tipo_combustivel": tipo_combustivel}
            )
            return (
                jsonify(
                    {
                        "status": "ok",
                        "mensagem": "Combustível criado com sucesso",
                    }
                ),
                201,
            )
        except Exception as erro:
            tb = traceback.format_exc()
            return (
                jsonify(
                    {
                        "status": "erro",
                        "mensagem": "Erro ao criar combustível",
                        "erro": str(erro),
                        "traceback": tb,
                    }
                ),
                500,
            )

    def buscar_todos_combustiveis(self):
        try:
            combustiveis = CombustivelService().buscar_todos_combustiveis()
            if combustiveis:
                combustiveis = [combustivel.to_dict() for combustivel in combustiveis]
                return (
                    jsonify(
                        {
                            "status": "ok",
                            "mensagem": "Combustíveis encontrados",
                            "dados": combustiveis,
                        }
                    ),
                    200,
                )
            else:
                return (
                    jsonify(
                        {"status": "erro", "mensagem": "Nenhum combustível encontrado"}
                    ),
                    404,
                )
        except Exception as erro:
            return (
                jsonify(
                    {
                        "status": "erro",
                        "mensagem": "Erro ao buscar combustíveis",
                        "erro": str(erro),
                    }
                ),
                500,
            )

    def buscar_combustivel_por_id(self, id_combustivel: int):
        try:
            combustivel = CombustivelService().buscar_combustivel_por_id(id_combustivel)
            if combustivel:
                combustivel = combustivel.to_dict()
                return (
                    jsonify(
                        {
                            "status": "ok",
                            "mensagem": "Combustível encontrado",
                            "dados": combustivel,
                        }
                    ),
                    200,
                )
            else:
                return (
                    jsonify(
                        {"status": "erro", "mensagem": "Combustível não encontrado"}
                    ),
                    404,
                )
        except Exception as erro:
            return (
                jsonify(
                    {
                        "status": "erro",
                        "mensagem": "Erro ao buscar combustível",
                        "erro": str(erro),
                    }
                ),
                500,
            )

    def buscar_combustivel_por_nome(self, nome_combustivel: str):
        try:
            combustivel = CombustivelService().buscar_combustivel_por_nome(
                nome_combustivel
            )
            if combustivel:
                combustivel = combustivel.to_dict()
                return (
                    jsonify(
                        {
                            "status": "ok",
                            "mensagem": "Combustível encontrado",
                            "dados": combustivel,
                        }
                    ),
                    200,
                )
            else:
                return (
                    jsonify(
                        {"status": "erro", "mensagem": "Combustível não encontrado"}
                    ),
                    404,
                )
        except Exception as erro:
            return (
                jsonify(
                    {
                        "status": "erro",
                        "mensagem": "Erro ao buscar combustível",
                        "erro": str(erro),
                    }
                ),
                500,
            )

    def atualizar_combustivel(self, id_combustivel: int):
        tipo_combustivel = request.form.get("tipo_combustivel")
        try:
            combustivel = CombustivelService().atualizar_combustivel(
                id_combustivel, {"tipo_combustivel": tipo_combustivel}
            )
            return (
                jsonify(
                    {"status": "ok", "mensagem": "Combustível atualizado com sucesso"}
                ),
                200,
            )
        except Exception as erro:
            return (
                jsonify(
                    {
                        "status": "erro",
                        "mensagem": "Erro ao atualizar combustível",
                        "erro": str(erro),
                    }
                ),
                500,
            )

    def deletar_combustivel(self, id_combustivel: int):
        try:
            combustivel = CombustivelService().deletar_combustivel(id_combustivel)
            return jsonify(
                {"status": "ok", "mensagem": "Combustível deletado com sucesso"}
            )
        except Exception as erro:
            return (
                jsonify(
                    {
                        "status": "erro",
                        "mensagem": "Erro ao deletar combustível",
                        "erro": str(erro),
                    }
                ),
                500,
            )

    def buscar_por_nome_semelhante(self, nome_combustivel: str):
        try:
            combustiveis = CombustivelService().buscar_por_nome_semelhante(
                nome_combustivel
            )
            if combustiveis:
                combustiveis = [combustivel.to_dict() for combustivel in combustiveis]
                return (
                    jsonify(
                        {
                            "status": "ok",
                            "mensagem": "Combustíveis encontrados",
                            "dados": combustiveis,
                        }
                    ),
                    200,
                )
            else:
                return (
                    jsonify(
                        {"status": "erro", "mensagem": "Nenhum combustível encontrado"}
                    ),
                    404,
                )
        except Exception as erro:
            return (
                jsonify(
                    {
                        "status": "erro",
                        "mensagem": "Erro ao buscar combustíveis",
                        "erro": str(erro),
                    }
                ),
                500,
            )
