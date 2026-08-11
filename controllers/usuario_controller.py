from flask import request, jsonify

from services.usuario_service import UsuarioService
from services.chamado_service import ChamadoService


class UsuarioController:

    @staticmethod
    def listar():
        usuarios = UsuarioService.listar()

        resultado = []

        for usuario in usuarios:
            resultado.append({
                "id": usuario.id,
                "nome": usuario.nome,
                "email": usuario.email,
                "setor": usuario.setor
            })

        return jsonify(resultado), 200

    @staticmethod
    def buscar(id):
        usuario = UsuarioService.buscar_por_id(id)

        if not usuario:
            return jsonify({
                "erro": "Usuário não encontrado"
            }), 404

        return jsonify({
            "id": usuario.id,
            "nome": usuario.nome,
            "email": usuario.email,
            "setor": usuario.setor
        }), 200

    @staticmethod
    def cadastrar():

        dados = request.json

        if not dados:
            return jsonify({
                "erro": "JSON inválido"
            }), 400

        usuario, erro = UsuarioService.cadastrar(
            dados.get("nome"),
            dados.get("email"),
            dados.get("setor")
        )

        if erro:
            return jsonify({
                "erro": erro
            }), 400

        return jsonify({
            "mensagem": "Usuário cadastrado",
            "id": usuario.id
        }), 201

    @staticmethod
    def atualizar(id):

        dados = request.json

        if not dados:
            return jsonify({
                "erro": "JSON inválido"
            }), 400

        usuario, erro = UsuarioService.atualizar(
            id,
            dados.get("nome"),
            dados.get("email"),
            dados.get("setor")
        )

        if erro:
            if erro == "Usuário não encontrado":
                return jsonify({
                    "erro": erro
                }), 404

            return jsonify({
                "erro": erro
            }), 400

        return jsonify({
            "mensagem": "Usuário atualizado"
        }), 200

    @staticmethod
    def excluir(id):

        sucesso, erro = UsuarioService.excluir(id)

        if erro:
            if erro == "Usuário não encontrado":
                return jsonify({
                    "erro": erro
                }), 404

            return jsonify({
                "erro": erro
            }), 400

        return jsonify({
            "mensagem": "Usuário removido"
        }), 200

    @staticmethod
    def chamados(id):

        chamados, erro = ChamadoService.listar_por_usuario(id)

        if erro:
            return jsonify({
                "erro": erro
            }), 404

        resultado = []

        for chamado in chamados:
            resultado.append({
                "id": chamado.id,
                "titulo": chamado.titulo,
                "descricao": chamado.descricao,
                "prioridade": chamado.prioridade,
                "status": chamado.status,
                "tecnico": chamado.tecnico,
                "data_abertura": chamado.data_abertura.strftime(
                    "%d/%m/%Y %H:%M"
                ),
                "usuario_id": chamado.usuario_id
            })

        return jsonify(resultado), 200