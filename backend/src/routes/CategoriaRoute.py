from flask import Blueprint
from src.controllers.CategoriaController import CategoriaController

categoria_bp = Blueprint("categorias", __name__)


@categoria_bp.route("/", methods=["POST"])
def criar_categoria():
    return CategoriaController().criar_categoria()

@categoria_bp.route("/", methods=["GET"])
def buscar_todas_categorias():
    return CategoriaController().buscar_todas_categorias()

@categoria_bp.route("/<int:id_categoria>", methods=["GET"])
def buscar_categoria_por_id(id_categoria: int):
    return CategoriaController().buscar_categoria_por_id(id_categoria)

@categoria_bp.route("/nome/<string:nome_categoria>", methods=["GET"])
def buscar_categoria_por_nome(nome_categoria: str):
    return CategoriaController().buscar_categoria_por_nome(nome_categoria)

@categoria_bp.route("/<int:id_categoria>", methods=["PUT"])
def atualizar_categoria(id_categoria: int):
    return CategoriaController().atualizar_categoria(id_categoria)

@categoria_bp.route("/<int:id_categoria>", methods=["DELETE"])
def deletar_categoria(id_categoria: int):
    return CategoriaController().deletar_categoria(id_categoria)

@categoria_bp.route("/buscar/<string:nome_categoria>", methods=["GET"])
def buscar_por_nome_semelhante(nome_categoria: str):
    return CategoriaController().buscar_por_nome_semelhante(nome_categoria)