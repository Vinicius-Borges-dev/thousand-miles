from flask import Blueprint, request, jsonify
from src.controllers.UsuarioController import UsuarioController
from src.middlewares.UsuarioMiddleware import UsuarioMiddleware

usuario_bp = Blueprint("Usuario_bp", __name__)

@usuario_bp.route("/cadastrar", methods=["POST"])
@UsuarioMiddleware.verificar_email
@UsuarioMiddleware.verificar_documentos
def cadastrar_usuario():
    return UsuarioController().cadastrar_usuario()