from flask import Blueprint, request, jsonify, Response
import base64
from PIL import Image
from io import BytesIO

vehicle_bp = Blueprint('vehicle_bp', __name__)

@vehicle_bp.route('/')
def index():
    return jsonify({
        'message': 'Tudo ok com a rota vehicles'
    })

@vehicle_bp.route('/create', methods=['POST'])
def create():
    brand = request.get_json()['brand']
    model = request.get_json()['model']
    category = request.get_json()['category']
    year = request.get_json()['year']
    color = request.get_json()['color']
    pricePerDay = request.get_json()['pricePerDay']
    apresentationPhoto = request.get_json()['apresentationPhoto']
    lateralPhoto = request.get_json()['lateralPhoto']
    
    return jsonify({
        'Chegou': apresentationPhoto
    })