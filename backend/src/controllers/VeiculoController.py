from src.services.VeiculoService import VeiculoService
from flask import request, jsonify


class VeiculoController:

    def cadastrar_veiculo(self):
        try:
            ano_fabricacao = request.json.get("ano_fabricacao")
            assentos = request.json.get("assentos")
            cor = request.json.get("cor")
            disponivel = 1
            placa = request.json.get("placa")
            preco_por_dia = request.json.get("preco_por_dia")
            id_album_veiculo = request.json.get("id_album_veiculo")
            id_categoria = request.json.get("id_categoria")
            id_cambio = request.json.get("id_cambio")
            id_combustivel = request.json.get("id_combustivel")
            id_modelo = request.json.get("id_modelo")

            veiculo = VeiculoService().criar_veículo(
                {
                    "ano_fabricacao": ano_fabricacao,
                    "assentos": assentos,
                    "cor": cor,
                    "disponivel": disponivel,
                    "placa": placa,
                    "preco_por_dia": preco_por_dia,
                    "id_album_veiculo": id_album_veiculo,
                    "id_categoria": id_categoria,
                    "id_cambio": id_cambio,
                    "id_combustivel": id_combustivel,
                    "id_modelo": id_modelo,
                }
            )
            return (
                jsonify(
                    {
                        "status": "ok",
                        "mensagem": "Veículo cadastrado com sucesso",
                    }
                ),
                201,
            )
        except Exception as erro:
            raise erro

    def buscar_veículo_por_placa(self, placa:str):
        try:
            veiculo = VeiculoService().buscar_veiculo_por_placa(placa)
            return veiculo
        except Exception as erro:
            raise erro

    def buscar_veículo_por_modelo(self, modelo:str):
        try:
            veiculo = VeiculoService().buscar_veiculo_por_modelo(modelo)
            return veiculo
        except Exception as erro:
            raise erro

    def buscar_veículo_por_id(self, id_veiculo: int):
        try:
            veiculo = VeiculoService().buscar_veiculo_por_id(id_veiculo)
            return veiculo
        except Exception as erro:
            raise erro

    def buscar_todos_veículos(self):
        try:
            veiculos = VeiculoService().buscar_todos_veiculos()
            return veiculos
        except Exception as erro:
            raise erro

    def editar_veículo(self, id_veiculo: int):
        try:
            ano_fabricacao = request.json.get("ano_fabricacao")
            assentos = request.json.get("assentos")
            cor = request.json.get("cor")
            disponivel = request.json.get("disponivel")
            placa = request.json.get("placa")
            preco_por_dia = request.json.get("preco_por_dia")
            id_album_veiculo = request.json.get("id_album_veiculo")
            id_categoria = request.json.get("id_categoria")
            id_cambio = request.json.get("id_cambio")
            id_combustivel = request.json.get("id_combustivel")
            id_modelo = request.json.get("id_modelo")

            veiculo = VeiculoService().atualizar_veiculo(
                id_veiculo,
                {
                    "ano_fabricacao": ano_fabricacao,
                    "assentos": assentos,
                    "cor": cor,
                    "disponivel": disponivel,
                    "placa": placa,
                    "preco_por_dia": preco_por_dia,
                    "id_album_veiculo": id_album_veiculo,
                    "id_categoria": id_categoria,
                    "id_cambio": id_cambio,
                    "id_combustivel": id_combustivel,
                    "id_modelo": id_modelo,
                },
            )
            return (
                jsonify(
                    {
                        "status": "ok",
                        "mensagem": "Veículo editado com sucesso",
                    }
                ),
                200,
            )
        except Exception as erro:
            raise erro

    def buscar_veiculo_aleatorio(self):
        try:
            veiculo = VeiculoService().buscar_veiculo_aleatorio_disponivel()
            return veiculo
        except Exception as erro:
            raise erro

    def buscar_veiculos_por_categoria(self, categoria:str):
        try:
            veiculos = VeiculoService().buscar_todos_veiculos_por_categoria(categoria)

            return veiculos
        except Exception as erro:
            raise erro

    def buscar_veiculos_por_modelo(self, modelo:str):
        try:
            veiculos = VeiculoService().buscar_todos_veiculos_por_modelo(modelo)
            return veiculos
        except Exception as erro:
            raise erro

    def buscar_veiculos_por_cambio(self, cambio:str):
        cambio = request.json.get("nome_cambio")
        try:
            veiculos = VeiculoService().buscar_todos_veiculos_por_cambio(cambio)
            return veiculos
        except Exception as erro:
            raise erro

    def buscar_veiculos_por_combustivel(self, combustivel:str):
        try:
            veiculos = VeiculoService().buscar_todos_veiculos_por_combustivel(
                combustivel
            )
            return veiculos
        except Exception as erro:
            raise erro

    def alterar_disponibilidade(self, id_veiculo: int):
        disponibilidade = request.json.get("disponibilidade")
        try:
            veiculo = VeiculoService().alterar_disponibilidade_veiculo(
                id_veiculo, disponibilidade
            )
            return (
                jsonify(
                    {
                        "status": "ok",
                        "mensagem": "Disponibilidade alterada com sucesso",
                    }
                ),
                200,
            )
        except Exception as erro:
            raise erro

    def excluir_veiculo(self, id_veiculo: int):
        try:
            veiculo = VeiculoService().deletar_veiculo(id_veiculo)
            return (
                jsonify(
                    {
                        "status": "ok",
                        "mensagem": "Veículo excluído com sucesso",
                    }
                ),
                200,
            )
        except Exception as erro:
            raise erro
