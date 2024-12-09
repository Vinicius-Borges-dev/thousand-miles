from flask import request, jsonify, current_app as app
from src.services.AlbumVeiculoService import AlbumVeiculoService
from werkzeug.utils import secure_filename
import os
import traceback

class AlbumVeiculoController:

    def criar_album_veiculo(self):
        try:
            foto_apresentacao_primaria = request.files.get("foto_apresentacao_primaria")
            foto_apresentacao_secundaria = request.files.get(
                "foto_apresentacao_secundaria"
            )
            foto_apresentacao_terciaria = request.files.get(
                "foto_apresentacao_terciaria"
            )
            foto_principal = request.files.get("foto_principal")
            foto_secundaria = request.files.get("foto_secundaria")

            foto_apresentacao_primaria_path = os.path.join(
                app.config["UPLOAD_IMAGES_VEICULOS_FOLDER"],
                secure_filename(foto_apresentacao_primaria.filename),
            )
            foto_apresentacao_secundaria_path = os.path.join(
                app.config["UPLOAD_IMAGES_VEICULOS_FOLDER"],
                secure_filename(foto_apresentacao_secundaria.filename),
            )
            foto_apresentacao_terciaria_path = os.path.join(
                app.config["UPLOAD_IMAGES_VEICULOS_FOLDER"],
                secure_filename(foto_apresentacao_terciaria.filename),
            )
            foto_principal_path = os.path.join(
                app.config["UPLOAD_IMAGES_VEICULOS_FOLDER"], secure_filename(foto_principal.filename)
            )
            foto_secundaria_path = os.path.join(
                app.config["UPLOAD_IMAGES_VEICULOS_FOLDER"], secure_filename(foto_secundaria.filename)
            )

            foto_apresentacao_primaria.save(foto_apresentacao_primaria_path)
            foto_apresentacao_secundaria.save(foto_apresentacao_secundaria_path)
            foto_apresentacao_terciaria.save(foto_apresentacao_terciaria_path)
            foto_principal.save(foto_principal_path)
            foto_secundaria.save(foto_secundaria_path)

            album_veiculo = AlbumVeiculoService().criar_album_veiculo(
                {
                    "foto_apresentacao_primaria": foto_apresentacao_primaria_path.replace(
                        "\\", "/"
                    ),
                    "foto_apresentacao_secundaria": foto_apresentacao_secundaria_path.replace(
                        "\\", "/"
                    ),
                    "foto_apresentacao_terciaria": foto_apresentacao_terciaria_path.replace(
                        "\\", "/"
                    ),
                    "foto_principal": foto_principal_path.replace("\\", "/"),
                    "foto_secundaria": foto_secundaria_path.replace("\\", "/"),
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
            tb = traceback.format_exc()
            return jsonify(
                {
                    "status": "erro",
                    "mensagem": "Erro ao cadastrar álbum de veículo",
                    "erro": str(erro),
                    "traceback": tb,
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
                        "dados": album_veiculo.to_dict(),
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
            foto_apresentacao_primaria = request.files.get("foto_apresentacao_primaria")
            foto_apresentacao_secundaria = request.files.get(
                "foto_apresentacao_secundaria"
            )
            foto_apresentacao_terciaria = request.files.get(
                "foto_apresentacao_terciaria"
            )
            foto_principal = request.files.get("foto_principal")
            foto_secundaria = request.files.get("foto_secundaria")

            album_atual = AlbumVeiculoService().buscar_album_veiculo_por_id(
                id_album_veiculo
            )

            def deletar_arquivo(caminho):
                if os.path.exists(caminho):
                    os.remove(caminho)

            novas_fotos = {}
            if (
                foto_apresentacao_primaria
                and foto_apresentacao_primaria.filename
                != album_atual.foto_apresentacao_primaria
            ):
                deletar_arquivo(album_atual.foto_apresentacao_primaria)
                
                novas_fotos["foto_apresentacao_primaria"] = os.path.join(app.config['UPLOAD_IMAGES_VEICULOS_FOLDER'], secure_filename(
                    foto_apresentacao_primaria.filename
                )).replace("\\", "/")
                foto_apresentacao_primaria.save(
                    os.path.join(
                        app.config["UPLOAD_IMAGES_VEICULOS_FOLDER"],
                        secure_filename(foto_apresentacao_primaria.filename),
                    )
                )
            else:
                novas_fotos["foto_apresentacao_primaria"] = album_atual.foto_apresentacao_primaria

            if (
                foto_apresentacao_secundaria
                and foto_apresentacao_secundaria.filename
                != album_atual.foto_apresentacao_secundaria
            ):
                deletar_arquivo(album_atual.foto_apresentacao_secundaria)
                
                novas_fotos["foto_apresentacao_secundaria"] = os.path.join(app.config['UPLOAD_IMAGES_VEICULOS_FOLDER'], secure_filename(
                    foto_apresentacao_secundaria.filename
                )).replace("\\", "/")
                foto_apresentacao_secundaria.save(
                    os.path.join(
                        app.config["UPLOAD_IMAGES_VEICULOS_FOLDER"],
                        secure_filename(foto_apresentacao_secundaria.filename),
                    )
                )
            else:
                novas_fotos["foto_apresentacao_secundaria"] = album_atual.foto_apresentacao_secundaria

            if (
                foto_apresentacao_terciaria
                and foto_apresentacao_terciaria.filename
                != album_atual.foto_apresentacao_terciaria
            ):
                deletar_arquivo(album_atual.foto_apresentacao_terciaria)
                
                novas_fotos["foto_apresentacao_terciaria"] =  os.path.join(app.config['UPLOAD_IMAGES_VEICULOS_FOLDER'], secure_filename(
                    foto_apresentacao_terciaria.filename
                )).replace("\\", "/")
                foto_apresentacao_terciaria.save(
                    os.path.join(
                        app.config["UPLOAD_IMAGES_VEICULOS_FOLDER"],
                        secure_filename(foto_apresentacao_terciaria.filename),
                    )
                )
            else:
                novas_fotos["foto_apresentacao_terciaria"] = album_atual.foto_apresentacao_terciaria

            if foto_principal and foto_principal.filename != album_atual.foto_principal:
                deletar_arquivo(album_atual.foto_principal)
                
                novas_fotos["foto_principal"] =  os.path.join(app.config['UPLOAD_IMAGES_VEICULOS_FOLDER'], secure_filename(
                    foto_principal.filename
                )).replace("\\", "/")
                foto_principal.save(
                    os.path.join(
                        app.config["UPLOAD_IMAGES_VEICULOS_FOLDER"],
                        secure_filename(foto_principal.filename),
                    )
                )
            else:
                novas_fotos["foto_principal"] = album_atual.foto_principal

            if (
                foto_secundaria
                and foto_secundaria.filename != album_atual.foto_secundaria
            ):
                deletar_arquivo(album_atual.foto_secundaria)
                
                novas_fotos["foto_secundaria"] =  os.path.join(app.config['UPLOAD_IMAGES_VEICULOS_FOLDER'], secure_filename(
                    foto_secundaria.filename
                )).replace("\\", "/")
                foto_secundaria.save(
                    os.path.join(
                        app.config["UPLOAD_IMAGES_VEICULOS_FOLDER"],
                        secure_filename(foto_secundaria.filename),
                    )
                )
            else:
                novas_fotos["foto_secundaria"] = album_atual.foto_secundaria

            album_veiculo = AlbumVeiculoService().atualizar_album_veiculo(
                id_album_veiculo, novas_fotos
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
