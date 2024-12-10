from flask import Flask
from src.configs.banco_de_dados import BancoDeDados
import src.models

def create_app():
    app = Flask(__name__)

    banco_de_dados = BancoDeDados(app)
    banco_de_dados.criar_tabelas()
    
    from src.routes.UsuarioRoute import usuario_bp
    app.register_blueprint(usuario_bp, url_prefix="/usuario")
    
    from src.routes.AlbumVeiculoRoute import album_veiculo_bp
    app.register_blueprint(album_veiculo_bp, url_prefix="/album_veiculo")
    
    from src.routes.CambioRoute import cambio_bp
    app.register_blueprint(cambio_bp, url_prefix="/cambio")
    
    from src.routes.CategoriaRoute import categoria_bp
    app.register_blueprint(categoria_bp, url_prefix="/categoria")
    
    from src.routes.CombustivelRoute import combustivel_bp
    app.register_blueprint(combustivel_bp, url_prefix="/combustivel")
    
    from src.routes.ModeloRoute import modelo_bp
    app.register_blueprint(modelo_bp, url_prefix="/modelo")
    
    from src.routes.VeiculoRoute import veiculo_bp
    app.register_blueprint(veiculo_bp, url_prefix="/veiculo")
    
    from src.routes.MarcaRoute import marca_bp
    app.register_blueprint(marca_bp, url_prefix="/marca")

    return app
