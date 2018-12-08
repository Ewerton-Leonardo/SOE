from app import db


class Disciplina(db.Model):
    __tablename__ = 'disciplina'

    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    id_aluno = db.Column('id_aluno', db.Integer, db.ForeignKey('aluno.id'), nullable=False)
    nome = db.Column('nome', db.String(20), nullable=False)

    aluno = db.relationship('Aluno', foreign_keys=id_aluno)

    def __init__(self, id_aluno, nome):
        self.nome = nome
        self.id_aluno = id_aluno

    def __repr__(self):
        return '<Disciplina %s>' % self.nome
