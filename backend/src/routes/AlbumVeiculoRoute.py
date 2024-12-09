from flask import Blueprint
from src.controllers.AlbumVeiculoController import AlbumVeiculoController

album_veiculo_bp = Blueprint("album_veiculos", __name__)


@album_veiculo_bp.route("/", methods=["POST"])
def criar_album_veiculo():
    return AlbumVeiculoController().criar_album_veiculo()


@album_veiculo_bp.route("/<int:id_album>", methods=["GET"])
def buscar_album_por_id(id_album: int):
    return AlbumVeiculoController().buscar_album_veiculo_por_id(id_album)


@album_veiculo_bp.route("/<int:id_album>", methods=["GET"])
def buscar_album_por_id(id_album: int):
    return AlbumVeiculoController().buscar_album_veiculo_por_id(id_album)


@album_veiculo_bp.route("/<int:id_album>", methods=["PUT"])
def atualizar_album_por_id(id_album: int):
    return AlbumVeiculoController().atualizar_album_veiculo(id_album)


@album_veiculo_bp.route("/<int:id_album>", methods=["DELETE"])
def deletar_album_por_id(id_album: int):
    return AlbumVeiculoController().deletar_album_veiculo(id_album)
