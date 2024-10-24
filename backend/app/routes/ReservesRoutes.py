from flask import Blueprint, request, jsonify

reserves_bp = Blueprint("reserves", __name__)

@reserves_bp.route('/')
def index():
    pass

@reserves_bp.route('/create')
def register():
    pass

@reserves_bp.route('/update/<int:id>', methods=['PUT'])
def update(id):
    pass

@reserves_bp.route('/delete/<int:id>', methods=['DELETE'])
def delete(id):
    pass