from flask import Flask
from src.configs.banco_de_dados import BancoDeDados

def create_app():
    app = Flask(__name__)
    
    BancoDeDados(app).criar_tabelas()
    
    return app