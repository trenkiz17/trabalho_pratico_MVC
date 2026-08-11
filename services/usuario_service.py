from models.usuario import Usuario
from repositories.usuario_repository import UsuarioRepository
from repositories.chamado_repository import ChamadoRepository


class UsuarioService:

    @staticmethod
    def listar():
        return UsuarioRepository.listar()

    @staticmethod
    def buscar_por_id(usuario_id):
        return UsuarioRepository.buscar_por_id(usuario_id)

    @staticmethod
    def cadastrar(nome, email, setor):

        if not nome:
            return None, "Nome é obrigatório"

        if not email:
            return None, "E-mail é obrigatório"

        usuario = UsuarioRepository.buscar_por_email(email)

        if usuario:
            return None, "E-mail já cadastrado"

        usuario = Usuario(
            nome=nome,
            email=email,
            setor=setor
        )

        UsuarioRepository.salvar(usuario)

        return usuario, None

    @staticmethod
    def atualizar(usuario_id, nome, email, setor):

        usuario = UsuarioRepository.buscar_por_id(usuario_id)

        if not usuario:
            return None, "Usuário não encontrado"

        if not nome:
            return None, "Nome é obrigatório"

        if not email:
            return None, "E-mail é obrigatório"

        outro_usuario = UsuarioRepository.buscar_por_email(email)

        if outro_usuario and outro_usuario.id != usuario.id:
            return None, "E-mail já cadastrado"

        usuario.nome = nome
        usuario.email = email
        usuario.setor = setor

        UsuarioRepository.salvar(usuario)

        return usuario, None

    @staticmethod
    def excluir(usuario_id):

        usuario = UsuarioRepository.buscar_por_id(usuario_id)

        if not usuario:
            return False, "Usuário não encontrado"

        chamados = ChamadoRepository.listar_por_usuario(usuario_id)

        if chamados:
            return False, "Não é possível excluir um usuário que possui chamados"

        UsuarioRepository.excluir(usuario)

        return True, None