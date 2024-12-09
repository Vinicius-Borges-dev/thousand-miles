from flask import Blueprint
from src.controllers.MarcaController import MarcaController

marca_bp = Blueprint('marca_bp', __name__)

@marca_bp.route('/', methods=['POST'])
def criar_marca():
    return MarcaController().criar_marca()

@marca_bp.route('/', methods=['GET'])
def buscar_todas_marcas():
    return MarcaController().buscar_todas_marcas()

@marca_bp.route('/<int:id_marca>', methods=['GET'])
def buscar_marca_por_id(id_marca):
    return MarcaController().buscar_marca_por_id(id_marca)

@marca_bp.route('/<string:nome_marca>', methods=['GET'])
def buscar_marca_por_nome(nome_marca):
    return MarcaController().buscar_marca_por_nome(nome_marca)

@marca_bp.route('/<int:id_marca>', methods=['PUT'])
def atualizar_marca(id_marca):
    return MarcaController().atualizar_marca(id_marca)

@marca_bp.route('/<int:id_marca>', methods=['DELETE'])
def deletar_marca(id_marca):
    return MarcaController().deletar_marca(id_marca)

@marca_bp.route('/buscar/<string:nome_marca>', methods=['GET'])
def buscar_por_nome_semelhante(nome_marca):
    return MarcaController().buscar_por_nome_semelhante(nome_marca)