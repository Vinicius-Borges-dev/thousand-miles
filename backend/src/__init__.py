from flask import Flask
from src.configs.banco_de_dados import BancoDeDados
import src.models


def create_app():
    app = Flask(__name__)

    banco_de_dados = BancoDeDados(app)
    banco_de_dados.criar_tabelas()
    banco_de_dados.text(
        """
            CREATE VIEW dados_usuario AS
            SELECT U.id_usuario, CONCAT(DP.nome,' ',DP.sobrenome) as nome, U.email, U.senha, U.nivel_acesso, D.tipo_documento, D.numero_documento, E.rua, E.numero, B.nome_bairro, C.nome_cidade , ES.nome_estado FROM usuario U
            JOIN dados_pessoais DP ON U.fk_id_dados_pessoais = DP.id_dados_pessoais
            JOIN documento D ON DP.fk_id_documento = D.id_documento
            JOIN endereco E ON U.fk_id_endereco = E.id_endereco
            JOIN bairro B ON E.fk_id_bairro = B.id_bairro
            JOIN cidade C ON B.fk_id_cidade = C.id_cidade
            JOIN estado ES ON C.fk_id_estado = ES.id_estado
        """
    )

    return app
