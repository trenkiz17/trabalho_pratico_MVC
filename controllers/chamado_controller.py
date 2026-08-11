from flask import request, jsonify

from services.chamado_service import ChamadoService


class ChamadoController:

    @staticmethod
    def listar():

        chamados = ChamadoService.listar()

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

    @staticmethod
    def buscar(id):

        chamado = ChamadoService.buscar_por_id(id)

        if not chamado:
            return jsonify({
                "erro": "Chamado não encontrado"
            }), 404

        return jsonify({
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
        }), 200

    @staticmethod
    def cadastrar():

        dados = request.json

        if not dados:
            return jsonify({
                "erro": "JSON inválido"
            }), 400

        chamado, erro = ChamadoService.cadastrar(
            dados.get("titulo"),
            dados.get("descricao"),
            dados.get("prioridade"),
            dados.get("tecnico"),
            dados.get("usuario_id")
        )

        if erro:
            return jsonify({
                "erro": erro
            }), 400

        return jsonify({
            "mensagem": "Chamado cadastrado",
            "id": chamado.id
        }), 201

    @staticmethod
    def atualizar(id):

        dados = request.json

        if not dados:
            return jsonify({
                "erro": "JSON inválido"
            }), 400

        chamado, erro = ChamadoService.atualizar(
            id,
            dados.get("titulo"),
            dados.get("descricao"),
            dados.get("prioridade"),
            dados.get("tecnico")
        )

        if erro:
            if erro == "Chamado não encontrado":
                return jsonify({
                    "erro": erro
                }), 404

            return jsonify({
                "erro": erro
            }), 400

        return jsonify({
            "mensagem": "Chamado atualizado"
        }), 200

    @staticmethod
    def excluir(id):

        sucesso, erro = ChamadoService.excluir(id)

        if erro:
            return jsonify({
                "erro": erro
            }), 404

        return jsonify({
            "mensagem": "Chamado removido"
        }), 200

    @staticmethod
    def iniciar(id):

        sucesso, erro = ChamadoService.iniciar(id)

        if erro:
            if erro == "Chamado não encontrado":
                return jsonify({
                    "erro": erro
                }), 404

            return jsonify({
                "erro": erro
            }), 400

        return jsonify({
            "mensagem": "Chamado iniciado"
        }), 200

    @staticmethod
    def encerrar(id):

        sucesso, erro = ChamadoService.encerrar(id)

        if erro:
            if erro == "Chamado não encontrado":
                return jsonify({
                    "erro": erro
                }), 404

            return jsonify({
                "erro": erro
            }), 400

        return jsonify({
            "mensagem": "Chamado encerrado"
        }), 200

    @staticmethod
    def abertos():

        chamados = ChamadoService.listar_abertos()

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

    @staticmethod
    def prioridade_alta():

        chamados = ChamadoService.listar_prioridade_alta()

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
    @staticmethod
    def estatisticas():

        resultado = ChamadoService.estatisticas()

        return jsonify(resultado), 200