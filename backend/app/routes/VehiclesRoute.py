from flask import Blueprint, request, jsonify
from app.controllers.VehicleController import VehicleController


vehicle_bp = Blueprint("vehicle_bp", __name__)


@vehicle_bp.route("/")
def index():
    return VehicleController().index(jsonify)

@vehicle_bp.route("/create", methods=["POST"])
def create():

    return VehicleController().add_vehicle(request, jsonify)


@vehicle_bp.route("/<int:id>", methods=["GET"])
def show(id):
    return VehicleController().get_vehicle_by_id(id, jsonify)