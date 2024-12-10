from flask import Blueprint
from src.controllers.VeiculoController import VeiculoController
from src.middlewares.UsuarioMiddleware import UsuarioMiddleware


veiculo_bp = Blueprint("veiculos", __name__)


@veiculo_bp.route("/", methods=["POST"])
def cadastrar_veiculo():
    return VeiculoController().cadastrar_veiculo()


@veiculo_bp.route("/placa/<string:placa>", methods=["GET"])
def buscar_veiculo_por_placa(placa):
    return VeiculoController().buscar_veículo_por_placa(placa)


@veiculo_bp.route("/modelo/<string:modelo>", methods=["GET"])
def buscar_veiculo_por_modelo(modelo):
    return VeiculoController().buscar_veículo_por_modelo(modelo)


@veiculo_bp.route("/<int:id_veiculo>", methods=["GET"])
def buscar_veiculo_por_id(id_veiculo):
    return VeiculoController().buscar_veículo_por_id(id_veiculo)


@veiculo_bp.route("/", methods=["GET"])
def buscar_todos_veiculos():
    return VeiculoController().buscar_todos_veículos()


@veiculo_bp.route("/<int:id_veiculo>", methods=["PUT"])
def editar(id_veiculo):
    return VeiculoController().editar_veículo(id_veiculo)


@veiculo_bp.route("/aleatorio", methods=["GET"])
def buscar_veiculo_aleatorio():
    return VeiculoController().buscar_veiculo_aleatorio()


@veiculo_bp.route("/categoria/<string:categoria>", methods=["GET"])
def buscar_veiculo_por_categoria(categoria):
    return VeiculoController().buscar_veiculos_por_categoria(categoria)


@veiculo_bp.route("/cambio/<string:cambio>", methods=["GET"])
def buscar_veiculo_por_cambio(cambio):
    return VeiculoController().buscar_veiculos_por_cambio(cambio)


@veiculo_bp.route("/combustivel/<string:combustivel>", methods=["GET"])
def buscar_veiculo_por_combustivel(combustivel):
    return VeiculoController().buscar_veiculos_por_combustivel(combustivel)


@veiculo_bp.route("/disponibilidade/<int:id_veiculo>", methods=["PATCH"])
def atualizar_disponibilidade(id_veiculo):
    return VeiculoController().alterar_disponibilidade(id_veiculo)


@veiculo_bp.route("/<int:id_veiculo>", methods=["DELETE"])
def deletar_veiculo(id_veiculo):
    return VeiculoController().excluir_veiculo(id_veiculo)

@veiculo_bp.route("/disponiveis", methods=["GET"])
def buscar_veiculos_disponiveis():
    return VeiculoController().buscar_veiculo_por_modelo_disponiveis()