from flask import Blueprint, request, jsonify
from src.services.UsuarioService import UsuarioService
from src.services.DadosPessoaisService import DadosPessoaisService
from src.services.DocumentoService import DocumentoService

usuario_bp = Blueprint("Usuario_bp", __name__)

@usuario_bp.route("/cadastrar_usuario", methods=["POST"])
def cadastrar_usuario():
    dados = {
        "email": request.json.get("email"),
        "senha": request.json.get("senha"),
        "nivel_acesso": request.json.get("nivel_acesso"),
        "id_dados_pessoais": request.json.get("id_dados_pessoais"),
        "id_endereco": request.json.get("id_endereco"),
    }
    usuario = UsuarioService().criar_usuario(dados)
    return usuario

@usuario_bp.route("/cadastrar_dados_pessoais", methods=["POST"])
def cadastrar_dados_pessoais():
    dados = {
        "nome": request.json.get("nome"),
        "sobrenome": request.json.get("sobrenome"),
        "id_documento": request.json.get("id_documento"),
    }
    dados_pessoais = DadosPessoaisService().criar_dados_pessoais(dados)
    return dados_pessoais

@usuario_bp.route("/cadastrar_documento", methods=["POST"])
def cadastrar_documento():
    dados = {
        "numero_documento": request.json.get("numero_documento"),
        "tipo_documento": request.json.get("tipo_documento"),
    }
    documento = DocumentoService().criar_documento(dados)
    return str(documento)