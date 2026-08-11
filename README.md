# MVC API

API desenvolvida em Flask utilizando arquitetura em camadas, SQLAlchemy e banco de dados SQLite.

## Estrutura do projeto

```text
helpdesk/
├── controllers/
│   ├── usuario_controller.py
│   └── chamado_controller.py
├── services/
│   ├── usuario_service.py
│   └── chamado_service.py
├── repositories/
│   ├── usuario_repository.py
│   └── chamado_repository.py
├── models/
│   ├── usuario.py
│   └── chamado.py
├── database.py
├── app.py
└── helpdesk.db
```

## Tecnologias utilizadas

* Python
* Flask
* Flask-SQLAlchemy
* SQLite

## Instalação

Abra o terminal na pasta do projeto e execute:

```bash
pip install flask flask-sqlalchemy
```

## Execução

Execute:

```bash
python app.py
```

A API ficará disponível em:

```text
http://127.0.0.1:5000
```

## Endpoints

### Usuários

```text
GET    /usuarios
GET    /usuarios/<id>
POST   /usuarios
PUT    /usuarios/<id>
DELETE /usuarios/<id>
GET    /usuarios/<id>/chamados
```

### Chamados

```text
GET    /chamados
GET    /chamados/<id>
POST   /chamados
PUT    /chamados/<id>
DELETE /chamados/<id>
PATCH  /chamados/<id>/iniciar
PATCH  /chamados/<id>/encerrar
GET    /chamados/abertos
GET    /chamados/prioridade/alta
```

### Estatísticas

```text
GET    /estatisticas
```

## Banco de dados

A aplicação utiliza SQLite. O arquivo `helpdesk.db` é criado automaticamente pela aplicação na primeira execução.

## Arquitetura

A aplicação utiliza separação de responsabilidades:

```text
Controller
    ↓
Service
    ↓
Repository
    ↓
Model
    ↓
SQLite
```

### Controller

Recebe as requisições, obtém os dados enviados pelo cliente, chama os Services e retorna as respostas da API.

### Service

Implementa as regras de negócio e valida as operações.

### Repository

Realiza as consultas e operações no banco de dados utilizando SQLAlchemy.

### Model

Define as entidades e o relacionamento entre as tabelas do banco de dados.
