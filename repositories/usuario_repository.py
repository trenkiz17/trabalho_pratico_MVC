from models.usuario import Usuario


class UsuarioRepository:

    @staticmethod
    def listar():
        return Usuario.query.all()

    @staticmethod
    def buscar_por_id(usuario_id):
        return Usuario.query.get(usuario_id)

    @staticmethod
    def buscar_por_email(email):
        return Usuario.query.filter_by(email=email).first()

    @staticmethod
    def salvar(usuario):
        from models.database import db

        db.session.add(usuario)
        db.session.commit()

        return usuario

    @staticmethod
    def excluir(usuario):
        from models.database import db

        db.session.delete(usuario)
        db.session.commit()
        
    
    @staticmethod
    def contar_total():
        return Usuario.query.count()