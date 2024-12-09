from flask import Blueprint
from src.controllers.CombustivelController import CombustivelController

combustivel_bp = Blueprint("combustiveis", __name__)


@combustivel_bp.route("/", methods=["POST"])
def criar_combustivel():
    return CombustivelController().criar_combustivel()


@combustivel_bp.route("/", methods=["GET"])
def buscar_todos_combustiveis():
    return CombustivelController().buscar_todos_combustiveis()


@combustivel_bp.route("/<int:id_combustivel>", methods=["GET"])
def buscar_combustivel_por_id(id_combustivel: int):
    return CombustivelController().buscar_combustivel_por_id(id_combustivel)


@combustivel_bp.route("/nome/<string:nome_combustivel>", methods=["GET"])
def buscar_combustivel_por_nome(nome_combustivel: str):
    return CombustivelController().buscar_combustivel_por_nome(nome_combustivel)


@combustivel_bp.route("/<int:id_combustivel>", methods=["PUT"])
def atualizar_combustivel(id_combustivel: int):
    return CombustivelController().atualizar_combustivel(id_combustivel)


@combustivel_bp.route("/<int:id_combustivel>", methods=["DELETE"])
def deletar_combustivel(id_combustivel: int):
    return CombustivelController().deletar_combustivel(id_combustivel)


@combustivel_bp.route("/buscar/<string:nome_combustivel>", methods=["GET"])
def buscar_por_nome_semelhante(nome_combustivel: str):
    return CombustivelController().buscar_por_nome_semelhante(nome_combustivel)
