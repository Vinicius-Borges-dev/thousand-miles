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
            usuario = {
                "email": request.json.get("email"),
                "senha": request.json.get("senha"),
                "nivel_acesso": "usuario",
            }
            dados_pessoais = {
                "nome": request.json.get("nome"),
                "sobrenome": request.json.get("sobrenome"),
                "data_nascimento": request.json.get("data_nascimento"),
            }
            documentos = {
                "cpf": request.json.get("cpf"),
                "rg": request.json.get("rg"),
            }
            endereco = {
                "rua": request.json.get("rua"),
                "numero": request.json.get("numero"),
            }
            bairro = {
                "nome_bairro": request.json.get("nome_bairro"),
            }
            cidade = {
                "nome_cidade": request.json.get("nome_cidade"),
            }
            estado = {
                "nome_estado": request.json.get("nome_estado"),
            }
            """ print(usuario)
            print(dados_pessoais)
            print(documentos)
            print(endereco)
            print(bairro)
            print(cidade)
            print(estado) """
            
            estado_check = EstadoService().capturar_estado_por_nome(estado.get("nome_estado"))
            if not estado_check:
                estado = EstadoService().criar_estado({
                    "nome_estado": estado.get("nome_estado")
                })
            
            cidade_check = CidadeService().capturar_cidade_por_nome(cidade.get("nome_cidade"))
            if not cidade_check:
                cidade = CidadeService().criar_cidade({
                    "nome_cidade": cidade.get("nome_cidade"),
                    "id_estado": estado.id_estado
                })
            
            bairro_check = BairroService().capturar_bairro_por_nome(bairro.get("nome_bairro"))
            if not bairro_check:
                bairro = BairroService().criar_bairro({
                    "nome_bairro": bairro.get("nome_bairro"),
                    "id_cidade": cidade.id_cidade
                })
            
            endereco_check = EnderecoService().capturar_endereco_por_rua_e_numero(endereco.get("rua"), endereco.get("numero"))
            if not endereco_check:
                endereco = EnderecoService().criar_endereco({
                    "rua": endereco_check.get("rua"),
                    "numero": endereco_check.get("numero"),
                    "id_bairro": bairro_check.id_bairro
                })
            
            documentos_check = DocumentoService().criar_documento(documentos)
            dados_pessoais_check = DadosPessoaisService().criar_dados_pessoais({
                "nome": dados_pessoais.get("nome"),
                "sobrenome": dados_pessoais.get("sobrenome"),
                "data_nascimento": dados_pessoais_check.get("data_nascimento"),
                "id_documento": documentos_check.id_documento
            })
            usuario = UsuarioService().criar_usuario({
                "email": usuario.get("email"),
                "senha": usuario.get("senha"),
                "nivel_acesso": usuario.get("nivel_acesso"),
                "id_dados_pessoais": dados_pessoais_check.id_dados_pessoais,
                "id_endereco": endereco_check.id_endereco
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