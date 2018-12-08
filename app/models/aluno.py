from app import db
from app import lm
from datetime import date


@lm.user_loader
def load_user(user_id):
    return Aluno.query.filter(Aluno.id == user_id).first()


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
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def __repr__(self):
        return '<Aluno %s>' % self.username
