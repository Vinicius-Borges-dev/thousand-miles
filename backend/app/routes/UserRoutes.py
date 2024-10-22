from flask import Blueprint, request, jsonify
from app.controllers.UserController import UserController

user_bp = Blueprint("user",__name__)

@user_bp.route("/register", methods={'POST'})
def create_user():
    return UserController().create_user(request, jsonify)

@user_bp.route("/login", methods=["POST"])
def get_by_id():
    return UserController().login(request, jsonify)