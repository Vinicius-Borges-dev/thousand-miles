from src.services.VeiculoService import VeiculoService
from flask import request, jsonify
from src.models.VeiculoModel import VeiculoModel
import traceback

class VeiculoController:

    def cadastrar_veiculo(self):
        try:
            ano_fabricacao = request.form.get("ano_fabricacao")
            assentos = request.form.get("assentos")
            cor = request.form.get("cor")
            disponivel = 1
            placa = request.form.get("placa")
            preco_por_dia = request.form.get("preco_por_dia")
            id_album_veiculo = request.form.get("id_album_veiculo")
            id_categoria = request.form.get("id_categoria")
            id_cambio = request.form.get("id_cambio")
            id_combustivel = request.form.get("id_combustivel")
            id_modelo = request.form.get("id_modelo")

            if not id_album_veiculo:
                id_album_veiculo = None

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

    def buscar_veículo_por_placa(self, placa: str):
        try:
            veiculo = VeiculoService().buscar_veiculo_por_placa(placa)
            if veiculo:
                veiculo = self.buscar_detalhes_do_veiculo(veiculo)
                return jsonify(
                    {
                        "status": "ok",
                        "dados": veiculo,
                        "mensagem": "Veículo encontrado com sucesso",
                    }
                )
            else:
                return (
                    jsonify(
                        {
                            "status": "erro",
                            "mensagem": "Veículo não encontrado",
                        }
                    ),
                    404,
                )
        except Exception as erro:
            return (
                jsonify(
                    {
                        "status": "erro",
                        "mensagem": "Erro ao buscar veículo",
                        "erro": str(erro),
                    }
                ),
                500,
            )

    def buscar_veículo_por_modelo(self, modelo: str):
        try:
            veiculo = VeiculoService().buscar_veiculo_por_modelo(modelo)
            if veiculo:
                veiculo = self.buscar_detalhes_do_veiculo(veiculo)
                return (
                    jsonify(
                        {
                            "status": "ok",
                            "dados": veiculo,
                            "mensagem": "Veículo encontrado com sucesso",
                        }
                    ),
                    200,
                )
            else:
                return (
                    jsonify(
                        {
                            "status": "erro",
                            "mensagem": "Veículo não encontrado",
                        }
                    ),
                    404,
                )

        except Exception as erro:
            return (
                jsonify(
                    {
                        "status": "erro",
                        "mensagem": "Erro ao buscar veículo",
                        "erro": str(erro),
                    }
                ),
                500,
            )

    def buscar_veículo_por_id(self, id_veiculo: int):
        try:
            veiculo = VeiculoService().buscar_veiculo_por_id(id_veiculo)
            if veiculo:
                veiculo = self.buscar_detalhes_do_veiculo(veiculo)
                return (
                    jsonify(
                        {
                            "status": "ok",
                            "dados": veiculo,
                            "mensagem": "Veículo encontrado com sucesso",
                        }
                    ),
                    200,
                )
            else:
                return (
                    jsonify(
                        {
                            "status": "erro",
                            "mensagem": "Veículo não encontrado",
                        }
                    ),
                    404,
                )

        except Exception as erro:
            return (
                jsonify(
                    {
                        "status": "erro",
                        "mensagem": "Erro ao buscar veículo",
                        "erro": str(erro),
                    }
                ),
                500,
            )

    def buscar_todos_veículos(self):
        try:
            veiculos = VeiculoService().buscar_todos_veiculos()
            if veiculos:
                veiculos = [
                    self.buscar_detalhes_do_veiculo(veiculo) for veiculo in veiculos
                ]
                return (
                    jsonify(
                        {
                            "status": "ok",
                            "dados": veiculos,
                            "mensagem": "Veículos encontrados com sucesso",
                        }
                    ),
                    200,
                )
            else:
                return (
                    jsonify(
                        {
                            "status": "erro",
                            "mensagem": "Veículos não encontrados",
                        }
                    ),
                    404,
                )
        except Exception as erro:
            return (
                jsonify(
                    {
                        "status": "erro",
                        "mensagem": "Erro ao buscar veículos",
                        "erro": str(erro),
                    }
                ),
                500,
            )

    def editar_veículo(self, id_veiculo: int):
        try:
            ano_fabricacao = request.form.get("ano_fabricacao")
            assentos = request.form.get("assentos")
            cor = request.form.get("cor")
            disponivel = 1
            placa = request.form.get("placa")
            preco_por_dia = request.form.get("preco_por_dia")
            id_album_veiculo = request.form.get("id_album_veiculo")
            id_categoria = request.form.get("id_categoria")
            id_cambio = request.form.get("id_cambio")
            id_combustivel = request.form.get("id_combustivel")
            id_modelo = request.form.get("id_modelo")

            if not id_album_veiculo:
                id_album_veiculo = None

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
            if veiculo:
                veiculo = self.buscar_detalhes_do_veiculo(veiculo)
                return (
                    jsonify(
                        {
                            "status": "ok",
                            "dados": veiculo,
                            "mensagem": "Veículo encontrado com sucesso",
                        }
                    ),
                    200,
                )
            else:
                return (
                    jsonify(
                        {
                            "status": "erro",
                            "mensagem": "Veículo não encontrado",
                        }
                    ),
                    404,
                )
        except Exception as erro:
            return (
                jsonify(
                    {
                        "status": "erro",
                        "mensagem": "Erro ao buscar veículo",
                        "erro": str(erro),
                    }
                ),
                500,
            )

    def buscar_veiculos_por_categoria(self, categoria: str):
        try:
            veiculos = VeiculoService().buscar_todos_veiculos_por_categoria(categoria)

            if veiculos:
                veiculos = [
                    self.buscar_detalhes_do_veiculo(veiculo) for veiculo in veiculos
                ]
                return (
                    jsonify(
                        {
                            "status": "ok",
                            "dados": veiculos,
                            "mensagem": "Veículos encontrados com sucesso",
                        }
                    ),
                    200,
                )
            else:
                return (
                    jsonify(
                        {
                            "status": "erro",
                            "mensagem": "Veículos não encontrados",
                        }
                    ),
                    404,
                )
        except Exception as erro:
            return (
                jsonify(
                    {
                        "status": "erro",
                        "mensagem": "Erro ao buscar veículos",
                        "erro": str(erro),
                    }
                ),
                500,
            )

    def buscar_veiculos_por_modelo(self, modelo: str):
        try:
            veiculos = VeiculoService().buscar_todos_veiculos_por_modelo(modelo)
            if veiculos:
                veiculos = [
                    self.buscar_detalhes_do_veiculo(veiculo) for veiculo in veiculos
                ]
                return (
                    jsonify(
                        {
                            "status": "ok",
                            "dados": veiculos,
                            "mensagem": "Veículos encontrados com sucesso",
                        }
                    ),
                    200,
                )
            else:
                return (
                    jsonify(
                        {
                            "status": "erro",
                            "mensagem": "Veículos não encontrados",
                        }
                    ),
                    404,
                )
        except Exception as erro:
            return (
                jsonify(
                    {
                        "status": "erro",
                        "mensagem": "Erro ao buscar veículos",
                        "erro": str(erro),
                    }
                ),
                500,
            )

    def buscar_veiculos_por_cambio(self, cambio: str):
        cambio = request.form.get("nome_cambio")
        try:
            veiculos = VeiculoService().buscar_todos_veiculos_por_cambio(cambio)
            if veiculos:
                veiculos = [
                    self.buscar_detalhes_do_veiculo(veiculo) for veiculo in veiculos
                ]
                return (
                    jsonify(
                        {
                            "status": "ok",
                            "dados": veiculos,
                            "mensagem": "Veículos encontrados com sucesso",
                        }
                    ),
                    200,
                )
            else:
                return (
                    jsonify(
                        {
                            "status": "erro",
                            "mensagem": "Veículos não encontrados",
                        }
                    ),
                    404,
                )
        except Exception as erro:
            return (
                jsonify(
                    {
                        "status": "erro",
                        "mensagem": "Erro ao buscar veículos",
                        "erro": str(erro),
                    }
                ),
                500,
            )

    def buscar_veiculos_por_combustivel(self, combustivel: str):
        try:
            veiculos = VeiculoService().buscar_todos_veiculos_por_combustivel(
                combustivel
            )
            if veiculos:
                veiculos = [
                    self.buscar_detalhes_do_veiculo(veiculo) for veiculo in veiculos
                ]
                return (
                    jsonify(
                        {
                            "status": "ok",
                            "dados": veiculos,
                            "mensagem": "Veículos encontrados com sucesso",
                        }
                    ),
                    200,
                )
            else:
                return (
                    jsonify(
                        {
                            "status": "erro",
                            "mensagem": "Veículos não encontrados",
                        }
                    ),
                    404,
                )
        except Exception as erro:
            return (
                jsonify(
                    {
                        "status": "erro",
                        "mensagem": "Erro ao buscar veículos",
                        "erro": str(erro),
                    }
                ),
                500,
            )

    def alterar_disponibilidade(self, id_veiculo: int):
        disponibilidade = request.form.get("disponibilidade")
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
            return (
                jsonify(
                    {
                        "status": "erro",
                        "mensagem": "Erro ao alterar disponibilidade",
                        "erro": str(erro),
                    }
                ),
                500,
            )

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
            return (
                jsonify(
                    {
                        "status": "erro",
                        "mensagem": "Erro ao excluir veículo",
                        "erro": str(erro),
                    }
                ),
                500,
            )

    def buscar_veiculo_por_modelo_disponiveis(self):
        try:
            veiculos = VeiculoService().buscar_veiculos_por_modelo_disponiveis()
            if veiculos:
                print(veiculos)
                veiculos = [
                    self.buscar_detalhes_do_veiculo(veiculo) for veiculo in veiculos
                ]
                return (
                    jsonify(
                        {
                            "status": "ok",
                            "dados": veiculos,
                            "mensagem": "Veículos encontrados com sucesso",
                        }
                    ),
                    200,
                )
            else:
                return (
                    jsonify(
                        {
                            "status": "erro",
                            "mensagem": "Veículos não encontrados",
                        }
                    ),
                    404,
                )

        except Exception as erro:
            tb = traceback.format_exc()
            return jsonify(
                {
                    "status": "erro",
                    "mensagem": "Erro ao buscar veículos",
                    "erro": str(erro),
                    "traceback": tb,
                }
            ), 500

    @staticmethod
    def buscar_detalhes_do_veiculo(veiculo: VeiculoModel):
        detalhes = {
            "id_veiculo": veiculo.id_veiculo,
            "ano_fabricacao": veiculo.ano_fabricacao,
            "assentos": veiculo.assentos,
            "cor": veiculo.cor,
            "disponivel": veiculo.disponivel,
            "placa": veiculo.placa,
            "preco_por_dia": veiculo.preco_por_dia,
            "album": {
                "id_album_veiculo": veiculo.modelo.album_veiculo.id_album_veiculo,
                "foto_apresentacao_primaria": veiculo.modelo.album_veiculo.foto_apresentacao_primaria,
                "foto_apresentacao_secundaria": veiculo.modelo.album_veiculo.foto_apresentacao_secundaria,
                "foto_apresentacao_terciaria": veiculo.modelo.album_veiculo.foto_apresentacao_terciaria,
                "foto_principal": veiculo.modelo.album_veiculo.foto_principal,
                "foto_secundaria": veiculo.modelo.album_veiculo.foto_secundaria,
            },
            "categoria": {
                "id_categoria": veiculo.categoria.id_categoria,
                "nome_categoria": veiculo.categoria.nome_categoria,
            },
            "cambio": {
                "id_cambio": veiculo.cambio.id_cambio,
                "tipo_cambio": veiculo.cambio.tipo_cambio,
            },
            "combustivel": {
                "id_combustivel": veiculo.combustivel.id_combustivel,
                "tipo_combustivel": veiculo.combustivel.tipo_combustivel,
            },
            "modelo": {
                "id_modelo": veiculo.modelo.id_modelo,
                "nome_modelo": veiculo.modelo.nome_modelo,
            },
            "marca": {
                "id_marca": veiculo.modelo.marca.id_marca,
                "nome_marca": veiculo.modelo.marca.nome_marca,
            },
        }
        return detalhes
