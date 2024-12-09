from flask import request, jsonify
from src.services.AlbumVeiculoService import AlbumVeiculoService


class AlbumVeiculoController:

    def criar_album_veiculo(self):
        try:
            foto_apresentacao_primaria = request.json.get("foto_apresentacao_primaria")
            foto_apresentacao_secundaria = request.json.get(
                "foto_apresentacao_secundaria"
            )
            foto_apresentacao_terciaria = request.json.get(
                "foto_apresentacao_terciaria"
            )
            foto_principal = request.json.get("foto_principal")
            foto_secundaria = request.json.get("foto_secundaria")
            album_veiculo = AlbumVeiculoService().criar_album_veiculo(
                {
                    "foto_apresentacao_primaria": foto_apresentacao_primaria,
                    "foto_apresentacao_secundaria": foto_apresentacao_secundaria,
                    "foto_apresentacao_terciaria": foto_apresentacao_terciaria,
                    "foto_principal": foto_principal,
                    "foto_secundaria": foto_secundaria,
                }
            )
            return (
                jsonify(
                    {
                        "status": "ok",
                        "mensagem": "Álbum de veículo cadastrado com sucesso",
                    }
                ),
                201,
            )
        except Exception as erro:
            return jsonify(
                {
                    "status": "erro",
                    "mensagem": "Erro ao cadastrar álbum de veículo",
                    "erro": str(erro),
                }
            )

    def buscar_album_veiculo_por_id(self, id_album_veiculo: int):
        try:
            album_veiculo = AlbumVeiculoService().buscar_album_veiculo_por_id(
                id_album_veiculo
            )
            if album_veiculo:
                return jsonify(
                    {
                        "status": "ok",
                        "mensagem": "Álbum de veículo encontrado",
                        "dados": album_veiculo,
                    }
                )
            else:
                return (
                    jsonify(
                        {
                            "status": "erro",
                            "mensagem": "Álbum de veículo não encontrado",
                        }
                    ),
                    404,
                )
        except Exception as erro:
            return (
                jsonify(
                    {
                        "status": "erro",
                        "mensagem": "Erro ao buscar álbum de veículo",
                        "erro": str(erro),
                    }
                ),
                500,
            )

    def atualizar_album_veiculo(self, id_album_veiculo: int):
        try:
            foto_apresentacao_primaria = request.json.get("foto_apresentacao_primaria")
            foto_apresentacao_secundaria = request.json.get(
                "foto_apresentacao_secundaria"
            )
            foto_apresentacao_terciaria = request.json.get(
                "foto_apresentacao_terciaria"
            )
            foto_principal = request.json.get("foto_principal")
            foto_secundaria = request.json.get("foto_secundaria")
            album_veiculo = AlbumVeiculoService().atualizar_album_veiculo(
                id_album_veiculo,
                {
                    "foto_apresentacao_primaria": foto_apresentacao_primaria,
                    "foto_apresentacao_secundaria": foto_apresentacao_secundaria,
                    "foto_apresentacao_terciaria": foto_apresentacao_terciaria,
                    "foto_principal": foto_principal,
                    "foto_secundaria": foto_secundaria,
                },
            )
            return (
                jsonify(
                    {
                        "status": "ok",
                        "mensagem": "Álbum de veículo atualizado com sucesso",
                    }
                ),
                200,
            )
        except Exception as erro:
            return (
                jsonify(
                    {
                        "status": "erro",
                        "mensagem": "Erro ao atualizar álbum de veículo",
                        "erro": str(erro),
                    }
                ),
                500,
            )

    def deletar_album_veiculo(self, id_album_veiculo: int):
        try:
            AlbumVeiculoService().deletar_album_veiculo(id_album_veiculo)
            return (
                jsonify(
                    {
                        "status": "ok",
                        "mensagem": "Álbum de veículo deletado com sucesso",
                    }
                ),
                200,
            )
        except Exception as erro:
            return (
                jsonify(
                    {
                        "status": "erro",
                        "mensagem": "Erro ao deletar álbum de veículo",
                        "erro": str(erro),
                    }
                ),
                500,
            )
