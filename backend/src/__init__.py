from flask import Flask
from src.configs.banco_de_dados import BancoDeDados
import src.models

def create_app():
    app = Flask(__name__)

    banco_de_dados = BancoDeDados(app)
    banco_de_dados.criar_tabelas()
    
    
    from src.routes.UsuarioRoute import usuario_bp
    app.register_blueprint(usuario_bp, url_prefix="/usuario")
    

    return app
