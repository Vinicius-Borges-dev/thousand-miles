from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, current_app as app
import os
from datetime import timedelta

Base = declarative_base()

banco_de_dados = SQLAlchemy()

class BancoDeDados:
    
    def __init__(self, app:Flask):
        self.__app = app
        self.__app.config.from_pyfile(os.path.join('configs', 'ambiente.py'))
        self.__nome_banco = self.__app.config.get("BANCO_DE_DADOS")
        self.__caminho_instancia = os.path.join(self.__app.instance_path, f"{self.__nome_banco}.sqlite3")
        os.makedirs(self.__app.instance_path, exist_ok=True)
        
        BD_URI = f"sqlite:///{self.__caminho_instancia}"
        self.__engine = create_engine(BD_URI)
        self.__Session = sessionmaker(bind=self.__engine)
        
        self.__app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
        self.__app.config['UPLOAD_IMAGES_MARCA_FOLDER'] = "src/uploads/imagens/marcas"
        self.__app.config['UPLOAD_IMAGES_VEICULOS_FOLDER'] = "src/uploads/imagens/veiculos"
        self.__app.config['SESSSION_PERMANENT'] = True
        self.__app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=4)
        self.__app.config['SQLALCHEMY_DATABASE_URI'] = BD_URI
        self.__app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        
        self.__app.session = self.__Session()
        self.__app.engine = self.__engine
        
        banco_de_dados.init_app(self.__app)

    def criar_tabelas(self):
        with self.__app.app_context():
            Base.metadata.create_all(self.__engine)
    
    def text(self, consulta:str)->list:
        with self.__app.engine.connect() as conexao:
            resultado = conexao.execute(text(consulta))
            if resultado.returns_rows:
                return resultado.fetchall()
            return None