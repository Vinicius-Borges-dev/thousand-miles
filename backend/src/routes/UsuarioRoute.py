from flask import Blueprint, request, jsonify
from src.controllers.UsuarioController import UsuarioController
from src.middlewares.AuthUsuarioMiddleware import AuthUsuarioMiddleware

usuario_bp = Blueprint("usuarios", __name__)

@usuario_bp.route("/cadastro", methods=["POST"])
@AuthUsuarioMiddleware.verificar_email
@AuthUsuarioMiddleware.verificar_documentos
def cadastrar_usuario():
    return UsuarioController().cadastrar_usuario()

@usuario_bp.route("/<int:id>", methods=["GET"])
@AuthUsuarioMiddleware.validar_existencia_token
@AuthUsuarioMiddleware.validar_dados_token
def buscar_usuario(id:int):
    return UsuarioController().capturar_informacoes_usuario(id)

@usuario_bp.route("/todos", methods=["GET"])
@AuthUsuarioMiddleware.validar_existencia_token
@AuthUsuarioMiddleware.validar_dados_token
@AuthUsuarioMiddleware.capturar_permissao_de_funcionario
def buscar_todos_usuarios():
    return UsuarioController().capturar_todos_usuarios()


@usuario_bp.route("/login", methods=["POST"])
def login():
    return UsuarioController().login_usuario()

@usuario_bp.route("/<int:id>", methods=["PUT"])
@AuthUsuarioMiddleware.validar_existencia_token
@AuthUsuarioMiddleware.validar_dados_token
def atualizar_usuario(id:int):
    return UsuarioController().atualizar_usuario(id)

@usuario_bp.route("/<int:id>", methods=["DELETE"])
@AuthUsuarioMiddleware.validar_existencia_token
@AuthUsuarioMiddleware.validar_dados_token
def deletar_usuario(id:int):
    return UsuarioController().deletar_usuario(id)