from flask import Blueprint
from src.controllers.CambioController import CambioController

cambio_bp = Blueprint("cambios", __name__)


@cambio_bp.route("/", methods=["POST"])
def criar_cambio():
    return CambioController().criar_cambio()


@cambio_bp.route("/", methods=["GET"])
def buscar_todos_cambios():
    return CambioController().buscar_todos_cambios()


@cambio_bp.route("/<int:id_cambio>", methods=["GET"])
def buscar_cambio_por_id(id_cambio: int):
    return CambioController().buscar_cambio_por_id(id_cambio)


@cambio_bp.route("/nome/<string:nome_cambio>", methods=["GET"])
def buscar_cambio_por_nome(nome_cambio: str):
    return CambioController().buscar_cambio_por_nome(nome_cambio)


@cambio_bp.route("/<int:id_cambio>", methods=["PUT"])
def atualizar_cambio(id_cambio: int):
    return CambioController().atualizar_cambio(id_cambio)


@cambio_bp.route("/<int:id_cambio>", methods=["DELETE"])
def deletar_cambio(id_cambio: int):
    return CambioController().deletar_cambio(id_cambio)


@cambio_bp.route("/buscar/<string:nome_cambio>", methods=["GET"])
def buscar_cambio_semelhante(nome_cambio: str):
    return CambioController().buscar_por_nome_semelhante(nome_cambio)
