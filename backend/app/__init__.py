from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()

def create_app():

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_thousand_miles.sqlite3'
    app.config['UPLOAD_FOLDER'] = 'app/static/uploads'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = "Thousand-Miles"

    db.init_app(app)
    CORS(app)
    
    from .routes.VehiclesRoute import vehicle_bp
    app.register_blueprint(vehicle_bp, url_prefix='/vehicles')

    return app