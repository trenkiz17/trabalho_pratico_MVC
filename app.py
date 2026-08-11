from flask import Flask

from models.database import db

from controllers.usuario_controller import UsuarioController
from controllers.chamado_controller import ChamadoController


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///helpdesk.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)


@app.route("/usuarios", methods=["GET"])
def listar_usuarios():
    return UsuarioController.listar()


@app.route("/usuarios/<int:id>", methods=["GET"])
def buscar_usuario(id):
    return UsuarioController.buscar(id)


@app.route("/usuarios", methods=["POST"])
def cadastrar_usuario():
    return UsuarioController.cadastrar()


@app.route("/usuarios/<int:id>", methods=["PUT"])
def atualizar_usuario(id):
    return UsuarioController.atualizar(id)


@app.route("/usuarios/<int:id>", methods=["DELETE"])
def excluir_usuario(id):
    return UsuarioController.excluir(id)


@app.route("/usuarios/<int:id>/chamados", methods=["GET"])
def listar_chamados_usuario(id):
    return UsuarioController.chamados(id)


@app.route("/chamados", methods=["GET"])
def listar_chamados():
    return ChamadoController.listar()


@app.route("/chamados/<int:id>", methods=["GET"])
def buscar_chamado(id):
    return ChamadoController.buscar(id)


@app.route("/chamados", methods=["POST"])
def cadastrar_chamado():
    return ChamadoController.cadastrar()


@app.route("/chamados/<int:id>", methods=["PUT"])
def atualizar_chamado(id):
    return ChamadoController.atualizar(id)


@app.route("/chamados/<int:id>", methods=["DELETE"])
def excluir_chamado(id):
    return ChamadoController.excluir(id)


@app.route("/chamados/<int:id>/iniciar", methods=["PATCH"])
def iniciar_chamado(id):
    return ChamadoController.iniciar(id)


@app.route("/chamados/<int:id>/encerrar", methods=["PATCH"])
def encerrar_chamado(id):
    return ChamadoController.encerrar(id)


@app.route("/chamados/abertos", methods=["GET"])
def chamados_abertos():
    return ChamadoController.abertos()


@app.route("/chamados/prioridade/alta", methods=["GET"])
def chamados_prioridade_alta():
    return ChamadoController.prioridade_alta()


@app.route("/estatisticas", methods=["GET"])
def estatisticas():
    return ChamadoController.estatisticas()

with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)