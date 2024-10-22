from flask import Flask
from flask_cors import CORS
from app.config.Database import Database
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "thousand-miles"
    app.config["UPLOAD_FOLDER"] = "app/static/uploads"
    CORS(app)

    Database.create_connection(app, db)

    from .routes.VehiclesRoute import vehicle_bp
    app.register_blueprint(vehicle_bp, url_prefix="/vehicles")
    
    from.routes.UserRoutes import user_bp
    app.register_blueprint(user_bp, url_prefix="/users")

    return app
