from models.chamado import Chamado


class ChamadoRepository:

    @staticmethod
    def listar():
        return Chamado.query.all()

    @staticmethod
    def buscar_por_id(chamado_id):
        return Chamado.query.get(chamado_id)

    @staticmethod
    def listar_por_usuario(usuario_id):
        return Chamado.query.filter_by(
            usuario_id=usuario_id
        ).all()

    @staticmethod
    def listar_abertos():
        return Chamado.query.filter_by(
            status="Aberto"
        ).all()

    @staticmethod
    def listar_prioridade_alta():
        return Chamado.query.filter_by(
            prioridade="Alta"
        ).all()

    @staticmethod
    def contar_nao_encerrados(usuario_id):
        return Chamado.query.filter(
            Chamado.usuario_id == usuario_id,
            Chamado.status != "Encerrado"
        ).count()

    @staticmethod
    def salvar(chamado):
        from models.database import db

        db.session.add(chamado)
        db.session.commit()

        return chamado

    @staticmethod
    def excluir(chamado):
        from models.database import db

        db.session.delete(chamado)
        db.session.commit()
    
    @staticmethod
    def contar_total():
        return Chamado.query.count()

    @staticmethod
    def contar_abertos():
        return Chamado.query.filter_by(
            status="Aberto"
        ).count()

    @staticmethod
    def contar_em_atendimento():
        return Chamado.query.filter_by(
            status="Em atendimento"
        ).count()

    @staticmethod
    def contar_encerrados():
        return Chamado.query.filter_by(
            status="Encerrado"
        ).count()    
    