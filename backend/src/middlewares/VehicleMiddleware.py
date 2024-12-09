from flask import request, jsonify
from src.services.VeiculoService import VeiculoService
from functools import wraps


class VeiculoMiddleware:
    
    @staticmethod
    def verificar_existencia_por_placa(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            placa = request.json.get("placa")
            veiculo = VeiculoService().buscar_veiculo_por_placa(placa)
            if veiculo:
                return jsonify({"mensagem": "Já existe um veículo cadastrado com essa placa."}), 409
            return f(*args, **kwargs)
        return wrapper
