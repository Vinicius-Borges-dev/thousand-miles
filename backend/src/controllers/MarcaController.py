from flask import request, jsonify, current_app as app
from src.services.MarcaService import MarcaService
import os
from werkzeug.utils import secure_filename
import traceback

class MarcaController:

    def criar_marca(self):
        nome_marca = request.form.get("nome_marca")
        logo_marca = request.files.get("logo_marca")

        logo_marca_path = os.path.join(
            app.config["UPLOAD_IMAGES_MARCA_FOLDER"],
            secure_filename(logo_marca.filename),
        )

        try:
            logo_marca.save(logo_marca_path)
            marca = MarcaService().criar_marca(
                {
                    "nome_marca": nome_marca,
                    "logo_marca": logo_marca_path.replace("\\", "/"),
                }
            )
            return (
                jsonify(
                    {
                        "status": "ok",
                        "mensagem": "Marca criada com sucesso",
                    }
                ),
                201,
            )
        except Exception as erro:
            return (
                jsonify(
                    {
                        "status": "erro",
                        "mensagem": "Erro ao criar marca",
                        "erro": str(erro),
                    }
                ),
                400,
            )

    def buscar_todas_marcas(self):
        try:
            marcas = MarcaService().buscar_todas_marcas()
            if marcas:
                return (
                    jsonify(
                        {
                            "status": "ok",
                            "mensagem": "Marcas encontradas",
                            "dados": [marca.to_dict() for marca in marcas],
                        }
                    ),
                    200,
                )
            else:
                return (
                    jsonify({"status": "erro", "mensagem": "Nenhuma marca encontrada"}),
                    404,
                )
        except Exception as erro:
            tb = traceback.format_exc()
            return (
                jsonify(
                    {
                        "status": "erro",
                        "mensagem": "Erro ao buscar marcas",
                        "erro": str(erro),
                        "traceback": tb,
                    }
                ),
                400,
            )

    def buscar_marca_por_id(self, id_marca):
        try:
            marca = MarcaService().buscar_marca_por_id(id_marca)
            if marca:
                return (
                    jsonify(
                        {
                            "status": "ok",
                            "mensagem": "Marca encontrada",
                            "dados": marca.to_dict(),
                        }
                    ),
                    200,
                )
            else:
                return (
                    jsonify({"status": "erro", "mensagem": "Marca não encontrada"}),
                    404,
                )
        except Exception as erro:
            return (
                jsonify(
                    {
                        "status": "erro",
                        "mensagem": "Erro ao buscar marca",
                        "erro": str(erro),
                    }
                ),
                400,
            )

    def buscar_marca_por_nome(self, nome_marca):
        try:
            marca = MarcaService().buscar_marca_por_nome(nome_marca)
            if marca:
                return (
                    jsonify(
                        {
                            "status": "ok",
                            "mensagem": "Marca encontrada",
                            "dados": marca.to_dict(),
                        }
                    ),
                    200,
                )
            else:
                return (
                    jsonify({"status": "erro", "mensagem": "Marca não encontrada"}),
                    404,
                )
        except Exception as erro:
            return (
                jsonify(
                    {
                        "status": "erro",
                        "mensagem": "Erro ao buscar marca",
                        "erro": str(erro),
                    }
                ),
                400,
            )

    def atualizar_marca(self, id_marca):
        nome_marca = request.form.get("nome_marca")
        logo_marca = request.files.get("logo_marca")
        logo_marca_path = os.path.join(
            app.config["UPLOAD_IMAGES_MARCA_FOLDER"],
            secure_filename(logo_marca.filename),
        )
        try:

            marca_atual = MarcaService().buscar_marca_por_id(id_marca)
            if logo_marca and logo_marca.filename != marca_atual.logo_marca:
                logo_marca.save(logo_marca_path)
                logo_marca = logo_marca_path.replace("\\", "/")
                if os.path.exists(marca_atual.logo_marca):
                    os.remove(marca_atual.logo_marca)

            marca = MarcaService().atualizar_marca(
                id_marca, {"nome_marca": nome_marca, "logo_marca": logo_marca}
            )
            return (
                jsonify({"status": "ok", "mensagem": "Marca atualizada com sucesso"}),
                200,
            )
        except Exception as erro:
            return (
                jsonify(
                    {
                        "status": "erro",
                        "mensagem": "Erro ao atualizar marca",
                        "erro": str(erro),
                    }
                ),
                400,
            )

    def deletar_marca(self, id_marca):
        try:
            MarcaService().deletar_marca(id_marca)
            return (
                jsonify({"status": "ok", "mensagem": "Marca deletada com sucesso"}),
                200,
            )
        except Exception as erro:
            return (
                jsonify(
                    {
                        "status": "erro",
                        "mensagem": "Erro ao deletar marca",
                        "erro": str(erro),
                    }
                ),
                400,
            )

    def buscar_por_nome_semelhante(self, nome_marca):
        try:
            marcas = MarcaService().buscar_marca_por_nome_semelhante(nome_marca)
            if marcas:
                return (
                    jsonify(
                        {
                            "status": "ok",
                            "mensagem": "Marcas encontradas",
                            "dados": [marca.to_dict() for marca in marcas],
                        }
                    ),
                    200,
                )
            else:
                return (
                    jsonify({"status": "erro", "mensagem": "Nenhuma marca encontrada"}),
                    404,
                )
        except Exception as erro:
            return (
                jsonify(
                    {
                        "status": "erro",
                        "mensagem": "Erro ao buscar marcas",
                        "erro": str(erro),
                    }
                ),
                400,
            )
