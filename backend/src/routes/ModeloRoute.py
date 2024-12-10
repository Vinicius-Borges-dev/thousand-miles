from flask import Blueprint
from src.controllers.ModeloController import ModeloController
from src.middlewares.AuthModeloMidleware import AuthModeloMiddleware

modelo_bp = Blueprint("modelos", __name__)

@modelo_bp.route("/", methods=["GET"])
def buscar_todos():
    return ModeloController().buscar_todos()

@modelo_bp.route("/", methods=["POST"])
@AuthModeloMiddleware.verificar_existencia_modelo
def criar_modelo():
    return ModeloController().criar_modelo()

@modelo_bp.route("/<int:id_modelo>", methods=["GET"])
def buscar_por_id(id_modelo: int):
    return ModeloController().buscar_por_id(id_modelo)

@modelo_bp.route("/nome/<string:nome>", methods=["GET"])
def buscar_por_nome(nome: str):
    return ModeloController().buscar_por_nome(nome)

@modelo_bp.route("/<int:id_modelo>", methods=["PUT"])
def editar_modelo(id_modelo: int):
    return ModeloController().editar_modelo(id_modelo)

@modelo_bp.route("/<int:id_modelo>", methods=["DELETE"])
def deletar_modelo(id_modelo: int):
    return ModeloController().excluir_modelo(id_modelo)

@modelo_bp.route("/buscar/<string:nome>", methods=["GET"])
def buscar_nome_semelhante(nome: str):
    return ModeloController().buscar_nome_semelhante(nome)