from flask import request, jsonify
from src.services.UsuarioService import UsuarioService
from src.services.EstadoService import EstadoService
from src.services.CidadeService import CidadeService
from src.services.BairroService import BairroService
from src.services.EnderecoService import EnderecoService
from src.services.DadosPessoaisService import DadosPessoaisService
from src.services.DocumentoService import DocumentoService

class UsuarioController:
    
    def cadastrar_usuario(self):
        try:
            email = request.json.get("email")
            senha = request.json.get("senha")
            nivel_acesso = "usuario"
            nome = request.json.get("nome")
            sobrenome = request.json.get("sobrenome")
            data_nascimento = request.json.get("data_nascimento")
            cpf = request.json.get("cpf")
            rg = request.json.get("rg")
            rua = request.json.get("rua")
            numero = request.json.get("numero")
            nome_bairro = request.json.get("nome_bairro")
            nome_cidade = request.json.get("nome_cidade")
            nome_estado = request.json.get("nome_estado")
            
            verificar_estado = EstadoService().capturar_estado_por_nome(nome_estado)
            if verificar_estado is None:
                EstadoService().criar_estado(estado)
                verificar_estado = EstadoService().capturar_estado_por_nome(estado.get("nome_estado"))
            
            verificar_cidade = CidadeService().capturar_cidade_por_nome(cidade.get("nome_cidade"))
            if verificar_cidade is None:
                CidadeService().criar_cidade(cidade)
                verificar_cidade = CidadeService().capturar_cidade_por_nome(cidade.get("nome_cidade"))
            
            verificar_bairro = BairroService().capturar_bairro_por_nome(bairro.get("nome_bairro"))
            if verificar_bairro is None:
                BairroService().criar_bairro(bairro)
                verificar_bairro = BairroService().capturar_bairro_por_nome(bairro.get("nome_bairro"))
            
            verificar_endereco = EnderecoService().capturar_endereco_por_rua_e_numero(endereco.get("rua"), endereco.get("numero"))
            if verificar_endereco is None:
                EnderecoService().criar_endereco(endereco)
                verificar_endereco = EnderecoService().capturar_endereco_por_rua_e_numero(endereco.get("rua"), endereco.get("numero"))
            
            novos_documentos = DocumentoService().criar_documento(documentos)
            novos_dados_pessoais = DadosPessoaisService().criar_dados_pessoais({
                "nome": dados_pessoais.get("nome"),
                "sobrenome": dados_pessoais.get("sobrenome"),
                "data_nascimento": dados_pessoais.get("data_nascimento"),
                "id_documento": novos_documentos.id_documento,
            })
            
            UsuarioService().criar_usuario({
                "email": usuario.get("email"),
                "senha": usuario.get("senha"),
                "nivel_acesso": usuario.get("nivel_acesso"),
                "id_dados_pessoais": novos_dados_pessoais.id_dados_pessoais,
                "id_endereco": verificar_endereco.id_endereco,
            })
            
            return jsonify({
                "status": "ok",
                "mensagem": "Usuário cadastrado com sucesso."
            }), 201
            
        except Exception as erro:
            raise erro
    
    @staticmethod
    def verificar_email(email):
        try:
            return UsuarioService().verificar_email(email)
        except Exception as erro:
            return jsonify({"mensagem":str(erro)}), 500

    @staticmethod
    def verificar_documentos(cpf, rg):
        try:
            teste = DocumentoService().verificar_documentos(cpf, rg)
            return teste
        except Exception as erro:
            return jsonify({"mensagem":str(erro)}), 500