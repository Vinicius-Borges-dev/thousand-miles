from src.services.ModeloService import ModeloService
from flask import request, jsonify
import traceback


class ModeloController:

    def criar_modelo(self):
        try:
            nome_modelo = request.form.get("nome_modelo")
            id_marca = request.form.get("id_marca")
            id_album_veiculo = request.form.get("id_album_veiculo")
            modelo = ModeloService().criar_modelo(
                {
                    "nome_modelo": nome_modelo,
                    "id_marca": id_marca,
                    "id_album_veiculo": id_album_veiculo,
                }
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
                modelo = {
                    "id_modelo": modelo.id_modelo,
                    "nome_modelo": modelo.nome_modelo,
                    "id_marca": modelo.marca.id_marca,
                    "nome_marca": modelo.marca.nome_marca,
                    "fotos": modelo.album_veiculo.to_dict(),
                }
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

    def buscar_por_nome(self, nome_modelo: str):
        try:
            modelo = ModeloService().buscar_modelo_por_nome(nome_modelo)
            if modelo:
                modelo = {
                    "id_modelo": modelo.id_modelo,
                    "nome_modelo": modelo.nome_modelo,
                    "id_marca": modelo.marca.id_marca,
                    "nome_marca": modelo.marca.nome_marca,
                    "fotos": modelo.album_veiculo.to_dict(),
                }
                return jsonify(
                    {"status": "ok", "mensagem": "Modelo encontrado", "dados": modelo}
                )
            else:
                return (
                    jsonify({"status": "erro", "mensagem": "Modelo não encontrado"}),
                    404,
                )
        except Exception as erro:
            tb = traceback.format_exc()
            return jsonify(
                {
                    "status": "erro",
                    "mensagem": "Erro ao buscar modelo",
                    "erro": str(erro),
                    "traceback": tb,
                }
            )

    def editar_modelo(self, id_modelo: int):
        try:
            nome_modelo = request.form.get("nome_modelo")
            id_marca = request.form.get("id_marca")
            id_album_veiculo = request.form.get("id_album_veiculo")
            modelo = ModeloService().atualizar_modelo(
                id_modelo,
                {
                    "nome_modelo": nome_modelo,
                    "id_marca": id_marca,
                    "id_album_veiculo": id_album_veiculo,
                },
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
                            "id_marca": modelo.marca.id_marca,
                            "nome_marca": modelo.marca.nome_marca,
                            "fotos": modelo.album_veiculo.to_dict(),
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
            tb = traceback.format_exc()
            return jsonify(
                {
                    "status": "erro",
                    "mensagem": "Erro ao buscar modelos",
                    "erro": str(erro),
                    "traceback": tb,
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
            modelos = ModeloService().buscar_nome_semelhate(nome_modelo)
            if modelos:
                lista = []
                for modelo in modelos:
                    lista.append(
                        {
                            "id_modelo": modelo.id_modelo,
                            "nome_modelo": modelo.nome_modelo,
                            "id_marca": modelo.marca.id_marca,
                            "nome_marca": modelo.marca.nome_marca,
                            "fotos": modelo.album_veiculo.to_dict(),
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
        
    
