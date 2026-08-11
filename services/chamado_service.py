from models.chamado import Chamado
from repositories.chamado_repository import ChamadoRepository
from repositories.usuario_repository import UsuarioRepository


class ChamadoService:

    @staticmethod
    def listar():
        return ChamadoRepository.listar()

    @staticmethod
    def buscar_por_id(chamado_id):
        return ChamadoRepository.buscar_por_id(chamado_id)

    @staticmethod
    def listar_por_usuario(usuario_id):

        usuario = UsuarioRepository.buscar_por_id(usuario_id)

        if not usuario:
            return None, "Usuário não encontrado"

        return ChamadoRepository.listar_por_usuario(usuario_id), None

    @staticmethod
    def listar_abertos():
        return ChamadoRepository.listar_abertos()

    @staticmethod
    def listar_prioridade_alta():
        return ChamadoRepository.listar_prioridade_alta()

    @staticmethod
    def cadastrar(
        titulo,
        descricao,
        prioridade,
        tecnico,
        usuario_id
    ):

        if not titulo:
            return None, "Título é obrigatório"

        if len(titulo) < 5:
            return None, "Título deve possuir pelo menos 5 caracteres"

        if not descricao:
            return None, "Descrição é obrigatória"

        if len(descricao) < 10:
            return None, "Descrição deve possuir pelo menos 10 caracteres"

        if prioridade not in ["Baixa", "Média", "Alta"]:
            return None, "Prioridade inválida"

        usuario = UsuarioRepository.buscar_por_id(usuario_id)

        if not usuario:
            return None, "Usuário não encontrado"

        quantidade = ChamadoRepository.contar_nao_encerrados(
            usuario_id
        )

        if quantidade >= 5:
            return None, "Usuário já possui cinco chamados não encerrados"

        chamado = Chamado(
            titulo=titulo,
            descricao=descricao,
            prioridade=prioridade,
            status="Aberto",
            tecnico=tecnico,
            usuario_id=usuario_id
        )

        ChamadoRepository.salvar(chamado)

        return chamado, None

    @staticmethod
    def atualizar(
        chamado_id,
        titulo,
        descricao,
        prioridade,
        tecnico
    ):

        chamado = ChamadoRepository.buscar_por_id(chamado_id)

        if not chamado:
            return None, "Chamado não encontrado"

        if titulo is not None:

            if len(titulo) < 5:
                return None, "Título deve possuir pelo menos 5 caracteres"

            chamado.titulo = titulo

        if descricao is not None:

            if len(descricao) < 10:
                return None, "Descrição deve possuir pelo menos 10 caracteres"

            chamado.descricao = descricao

        if prioridade is not None:

            if prioridade not in ["Baixa", "Média", "Alta"]:
                return None, "Prioridade inválida"

            chamado.prioridade = prioridade

        if tecnico is not None:
            chamado.tecnico = tecnico

        ChamadoRepository.salvar(chamado)

        return chamado, None

    @staticmethod
    def excluir(chamado_id):

        chamado = ChamadoRepository.buscar_por_id(chamado_id)

        if not chamado:
            return False, "Chamado não encontrado"

        ChamadoRepository.excluir(chamado)

        return True, None

    @staticmethod
    def iniciar(chamado_id):

        chamado = ChamadoRepository.buscar_por_id(chamado_id)

        if not chamado:
            return False, "Chamado não encontrado"

        if chamado.status != "Aberto":
            return False, "Só é possível iniciar um chamado aberto"

        chamado.status = "Em atendimento"

        ChamadoRepository.salvar(chamado)

        return True, None

    @staticmethod
    def encerrar(chamado_id):

        chamado = ChamadoRepository.buscar_por_id(chamado_id)

        if not chamado:
            return False, "Chamado não encontrado"

        if chamado.status != "Em atendimento":
            return False, "Só é possível encerrar um chamado em atendimento"

        chamado.status = "Encerrado"

        ChamadoRepository.salvar(chamado)

        return True, None
    
    @staticmethod
    def estatisticas():

        return {
            "usuarios": UsuarioRepository.contar_total(),
            "chamados": ChamadoRepository.contar_total(),
            "abertos": ChamadoRepository.contar_abertos(),
            "em_atendimento": ChamadoRepository.contar_em_atendimento(),
            "encerrados": ChamadoRepository.contar_encerrados()
        }