from app import db
from datetime import date


class Aluno(db.Model):
    __tablename__ = 'aluno'

    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    username = db.Column('username', db.String(20), nullable=False, unique=True)
    senha = db.Column('senha', db.String(30), nullable=False)
    nome = db.Column('nome', db.String(50), nullable=False)
    data_nasc = db.Column('data_nasc', db.Date, nullable=False)
    curso = db.Column('curso', db.String(20), nullable=False)

    def __init__(self,
                 username: str,
                 senha: str,
                 nome: str,
                 data_nasc: date,
                 curso: str):
        self.username = username
        self.senha = senha
        self.nome = nome
        self.data_nasc = data_nasc
        self.curso = curso

    @property
    def is_autheticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymus(self):
        return False

    def get_id(self):
        return str(self.id)


class Professor(db.Model):
    __tablename__ = 'professor'

    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    username = db.Column('username', db.String(20), nullable=False, unique=True)
    senha = db.Column('senha', db.String(30), nullable=False)
    nome = db.Column('nome', db.String(50), nullable=False)
    data_nasc = db.Column('data_nasc', db.Date, nullable=False)

    def __init__(self,
                 username: str,
                 senha: str,
                 nome: str,
                 data_nasc: date):
        self.username = username
        self.senha = senha
        self.nome = nome
        self.data_nasc = data_nasc

    @property
    def is_autheticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymus(self):
        return False

    def get_id(self):
        return str(self.id)


class Disciplina(db.Model):
    __tablename__ = 'disciplina'

    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column('nome', db.String(20), nullable=False)

    def __init__(self, nome):
        self.nome = nome


class Atividade(db.Model):
    __tablename__ = 'atividade'

    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column('nome', db.String(40), nullable=False)
    prazo_entrega = db.Column('prazo_entrega', db.DateTime, nullable=False)
    tag = db.Column('tag', db.String(20))
    nome_disciplina = db.Column('nome_disciplina', db.String, nullable=True)
    conteudo = db.Column('conteudo', db.Text, nullable=False)
    nivel_importancia = db.Column('nivel_importancia', db.String(1), nullable=False)

    def __init__(self, nome, prazo_entrega, tag, disciplina, conteudo, nivel_importancia):
        self.nome = nome
        self.prazo_entrega = prazo_entrega
        self.tag = tag
        self.disciplina = disciplina
        self.conteudo = conteudo
        self.nivel_importancia = nivel_importancia


class Horario(db.Model):
    __tablename__ = 'horario'

    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    nome_disciplina = db.Column('nome_disciplina', db.String, nullable=False)
    nome_professor = db.Column('nome_professor', db.String, nullable=False)
    dia = db.Column('dia', db.String(15), nullable=False)
    hora = db.Column('hora', db.Time, nullable=True)
    sala = db.Column('sala', db.String(20), nullable=True)

    def __init__(self, disciplina, professor, dia, hora, sala):
        self.disciplina = disciplina
        self.professor = professor
        self.dia = dia
        self.hora = hora
        self.sala = sala
