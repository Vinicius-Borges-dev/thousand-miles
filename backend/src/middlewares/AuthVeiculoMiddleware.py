from flask import request, jsonify
from src.controllers.VeiculoController import VeiculoController
from src.controllers.ModeloController import ModeloController
from src.controllers.MarcaController import MarcaController
from functools import wraps


class AuthVeiculoMiddleware:
    
    @staticmethod
    def verificar_existencia_placa(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            placa = request.form.get("placa")
            veiculo = VeiculoController().buscar_veículo_por_placa(placa)
            if veiculo[1]==200:
                return jsonify({"status": "erro", "mensagem": "Já existe um veículo cadastrado com essa placa."}), 409
            return f(*args, **kwargs)
        return wrapper
    
    
