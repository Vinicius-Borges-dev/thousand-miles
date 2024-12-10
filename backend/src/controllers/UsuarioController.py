from flask import request, jsonify
from src.services.UsuarioService import UsuarioService
from src.services.EstadoService import EstadoService
from src.services.CidadeService import CidadeService
from src.services.BairroService import BairroService
from src.services.EnderecoService import EnderecoService
from src.services.DadosPessoaisService import DadosPessoaisService
from src.services.DocumentoService import DocumentoService
import bcrypt
from datetime import datetime, timedelta
import jwt
from os import environ


class UsuarioController:

    def cadastrar_usuario(self):
        try:
            email = request.form.get("email")
            senha = request.form.get("senha")
            nivel_acesso = "admin"
            nome = request.form.get("nome")
            sobrenome = request.form.get("sobrenome")
            data_nascimento = request.form.get("data_nascimento")
            cpf = request.form.get("cpf")
            rg = request.form.get("rg")
            rua = request.form.get("rua")
            numero = request.form.get("numero")
            nome_bairro = request.form.get("nome_bairro")
            nome_cidade = request.form.get("nome_cidade")
            nome_estado = request.form.get("nome_estado")

            estado = self.verificar_ou_criar_estado(nome_estado)
            cidade = self.verificar_ou_criar_cidade(nome_cidade, estado.id_estado)
            bairro = self.verificar_ou_criar_bairro(nome_bairro, cidade.id_cidade)
            endereco = EnderecoService().capturar_endereco_por_rua_e_numero(rua, numero)

            if endereco is None:
                endereco = EnderecoService().criar_endereco(
                    {
                        "rua": rua,
                        "numero": numero,
                        "id_bairro": bairro.id_bairro,
                    }
                )

            documentos = DocumentoService().criar_documento({"cpf": cpf, "rg": rg})

            data_nascimento_formatada = datetime.strptime(data_nascimento, "%Y-%m-%d")

            dados_pessoais = DadosPessoaisService().criar_dados_pessoais(
                {
                    "nome": nome,
                    "sobrenome": sobrenome,
                    "data_nascimento": data_nascimento_formatada,
                    "id_documento": documentos.id_documento,
                }
            )

            senha_hash = self.senha_hash(senha)

            UsuarioService().criar_usuario(
                {
                    "email": email,
                    "senha": senha_hash,
                    "nivel_acesso": nivel_acesso,
                    "id_dados_pessoais": dados_pessoais.id_dados_pessoais,
                    "id_endereco": endereco.id_endereco,
                }
            )

            return (
                jsonify(
                    {"status": "ok", "mensagem": "Usuário cadastrado com sucesso."}
                ),
                201,
            )
        except Exception as erro:
            raise erro

    def login_usuario(self):
        try:
            email = request.form.get("email")
            senha = request.form.get("senha")

            usuario = UsuarioService().verificar_email(email)

            if not usuario:
                return (
                    jsonify({"status": "erro", "mensagem": "Usuário não encontrado."}),
                    404,
                )

            if not self.senha_check(senha, usuario.senha):
                return jsonify({"status": "erro", "mensagem": "Senha incorreta."}), 401

            token = self.gerar_token(usuario.id_usuario, usuario.nivel_acesso, usuario.dados_pessoais.nome, usuario.dados_pessoais.sobrenome)

            return (
                jsonify(
                    {
                        "status": "ok",
                        "mensagem": "Login realizado com sucesso",
                        "token": token,
                    }
                ),
                200,
            )

        except Exception as erro:
            raise erro

    def atualizar_usuario(self, id_usuario: int):
        email = request.form.get("email")
        nivel_acesso = "usuario"
        nome = request.form.get("nome")
        sobrenome = request.form.get("sobrenome")
        data_nascimento = request.form.get("data_nascimento")
        cpf = request.form.get("cpf")
        rg = request.form.get("rg")
        rua = request.form.get("rua")
        numero = request.form.get("numero")
        nome_bairro = request.form.get("nome_bairro")
        nome_cidade = request.form.get("nome_cidade")
        nome_estado = request.form.get("nome_estado")

        try:
            usuario = UsuarioService().capturar_informacoes_usuario(id_usuario)
            dados_pessoais = DadosPessoaisService().capturar_informacao_dados_pessoais(
                usuario.fk_id_dados_pessoais
            )
            documentos = DocumentoService().capturar_documento_por_id(
                dados_pessoais.fk_id_documento
            )
            endereco = EnderecoService().capturar_endereco_por_id(
                usuario.fk_id_endereco
            )
            bairro = BairroService().capturar_bairro_por_id(endereco.fk_id_bairro)
            cidade = CidadeService().capturar_cidade_por_id(bairro.fk_id_cidade)
            estado = EstadoService().capturar_estado_por_id(cidade.fk_id_estado)

            estado = self.verificar_ou_criar_estado(nome_estado)
            cidade = self.verificar_ou_criar_cidade(nome_cidade, estado.id_estado)
            bairro = self.verificar_ou_criar_bairro(nome_bairro, cidade.id_cidade)
            
            endereco = EnderecoService().atualizar_endereco(
                endereco.id_endereco,
                {"rua": rua, "numero": numero, "id_bairro": bairro.id_bairro},
            )
            
            documentos = DocumentoService().atualizar_documento(
                documentos.id_documento, {"cpf": cpf, "rg": rg}
            )
            
            data_nascimento_formatada = datetime.strptime(data_nascimento, "%Y-%m-%d")
            
            dados_pessoais = DadosPessoaisService().editar_dados_pessoais(
                dados_pessoais.id_dados_pessoais,
                {
                    "nome": nome,
                    "sobrenome": sobrenome,
                    "data_nascimento": data_nascimento_formatada,
                    "id_documento": documentos.id_documento,
                },
            )
            usuario = UsuarioService().editar_usuario(
                usuario.id_usuario,
                {
                    "email": email,
                    "senha": usuario.senha,
                    "nivel_acesso": nivel_acesso,
                    "id_dados_pessoais": dados_pessoais.id_dados_pessoais,
                    "id_endereco": endereco.id_endereco,
                },
            )

            return (
                jsonify(
                    {"status": "ok", "mensagem": "Usuário atualizado com sucesso."}
                ),
                200,
            )

        except Exception as erro:
            raise erro
    
    def deletar_usuario(self, id_usuario: int):
        try:

            UsuarioService().deletar_usuario(id_usuario)

            return (
                jsonify(
                    {"status": "ok", "mensagem": "Usuário deletado com sucesso."}
                ),
                200,
            )
        except Exception as erro:
            raise erro
        
    def capturar_informacoes_usuario(self, id_usuario:int):
        try:
            usuario = UsuarioService().capturar_informacoes_usuario(id_usuario)
            dados = {
                "id_usuario": usuario.id_usuario,
                "email": usuario.email,
                "nivel_acesso": usuario.nivel_acesso,
                "dados_pessoais": {
                    "nome": usuario.dados_pessoais.nome,
                    "sobrenome": usuario.dados_pessoais.sobrenome,
                    "data_nascimento": usuario.dados_pessoais.data_nascimento.strftime("%Y-%m-%d"),
                    "documentos": {
                        "cpf": usuario.dados_pessoais.documento.cpf,
                        "rg": usuario.dados_pessoais.documento.rg,
                    },
                },
                "endereco": {
                    "rua": usuario.endereco.rua,
                    "numero": usuario.endereco.numero,
                    "bairro": usuario.endereco.bairro.nome_bairro,
                    "cidade": usuario.endereco.bairro.cidade.nome_cidade,
                    "estado": usuario.endereco.bairro.cidade.estado.nome_estado,
                },
            }
            return jsonify(dados), 200
        except Exception as erro:
            raise erro
        
    def capturar_todos_usuarios(self):
        try:
            usuarios = UsuarioService().buscar_todos_usuarios()
            lista_usuarios = []
            for usuario in usuarios:
                lista_usuarios.append(
                    {
                        "id_usuario": usuario.id_usuario,
                        "nivel_acesso": usuario.nivel_acesso,
                        "dados_pessoais": {
                            "nome": usuario.dados_pessoais.nome,
                            "sobrenome": usuario.dados_pessoais.sobrenome,
                            "data_nascimento": usuario.dados_pessoais.data_nascimento.strftime("%Y-%m-%d"),
                        },
                        "endereco": {
                            "rua": usuario.endereco.rua,
                            "numero": usuario.endereco.numero,
                            "bairro": usuario.endereco.bairro.nome_bairro,
                            "cidade": usuario.endereco.bairro.cidade.nome_cidade,
                            "estado": usuario.endereco.bairro.cidade.estado.nome_estado,
                        },
                    }
                )
            return jsonify(lista_usuarios), 200
        except Exception as erro:
            raise erro

    @staticmethod
    def verificar_email(email):
        try:
            usuario = UsuarioService().verificar_email(email)

            return usuario
        except Exception as erro:
            return jsonify({"mensagem": str(erro)}), 500

    @staticmethod
    def verificar_documentos(cpf, rg):
        try:
            teste = DocumentoService().verificar_documentos(cpf, rg)
            return teste
        except Exception as erro:
            return jsonify({"mensagem": str(erro)}), 500

    @staticmethod
    def senha_hash(senha: str):
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(senha.encode("utf-8"), salt)

    @staticmethod
    def senha_check(senha: str, senha_hash: str) -> bool:
        return bcrypt.checkpw(senha.encode("utf-8"), senha_hash)

    @staticmethod
    def gerar_token(id_usuario: int, nivel_acesso: str, nome_usuario: str, sobrenome_usuario: str):
        dados = {
            "exp": datetime.utcnow() + timedelta(hours=1),
            "usuario": id_usuario,
            "nivel_acesso": nivel_acesso,
            "nome": nome_usuario,
            "sobrenome": sobrenome_usuario
        }

        chave = environ.get("SECRET_KEY")

        token = jwt.encode(dados, chave, algorithm="HS256")

        return token

    @staticmethod
    def verificar_ou_criar_estado(nome_estado):
        estado = EstadoService().capturar_estado_por_nome(nome_estado)
        if estado is None:
            EstadoService().criar_estado({"nome_estado": nome_estado})
            estado = EstadoService().capturar_estado_por_nome(nome_estado)
        return estado

    @staticmethod
    def verificar_ou_criar_cidade(nome_cidade, id_estado):
        cidade = CidadeService().capturar_cidade_por_nome(nome_cidade)
        if cidade is None:
            CidadeService().criar_cidade(
                {"nome_cidade": nome_cidade, "id_estado": id_estado}
            )
            cidade = CidadeService().capturar_cidade_por_nome(nome_cidade)
        return cidade

    @staticmethod
    def verificar_ou_criar_bairro(nome_bairro, id_cidade):
        bairro = BairroService().capturar_bairro_por_nome(nome_bairro)
        if bairro is None:
            BairroService().criar_bairro(
                {"nome_bairro": nome_bairro, "id_cidade": id_cidade}
            )
            bairro = BairroService().capturar_bairro_por_nome(nome_bairro)
        return bairro
