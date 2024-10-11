from flask import Blueprint, request, jsonify, Response

vehicle_bp = Blueprint('vehicle_bp', __name__)

@vehicle_bp.route('/')
def index():
    return jsonify({
        'message': 'Tudo ok com a rota vehicles'
    })

@vehicle_bp.route('/create', methods=['POST'])
def create():
    brand = request.form.get('brand')
    model = request.form.get('model')
    category = request.form.get('category')
    year = request.form.get('year')
    color = request.form.get('color')
    price_per_day = request.form.get('pricePerDay')
    description = request.form.get('description')

    apresentation_photo = request.files.get('apresentationPhoto')
    lateral_photo = request.files.get('lateralPhoto')


    return jsonify({
        'brand': brand,
        'model': model,
        'category': category,
        'year': year,
        'color': color,
        'pricePerDay': price_per_day,
        'description': description,
        'apresentationPhoto': str(apresentation_photo),
        'lateralPhoto': str(lateral_photo)
    })