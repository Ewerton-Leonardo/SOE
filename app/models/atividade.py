from app import db


class Atividade(db.Model):
    __tablename__ = 'atividade'

    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    id_aluno = db.Column('id_aluno', db.Integer, db.ForeignKey('aluno.id'), nullable=False)
    nome = db.Column('nome', db.String(40), nullable=False)
    prazo_entrega = db.Column('prazo_entrega', db.DateTime, nullable=False)
    tag = db.Column('tag', db.String(20))
    nome_disciplina = db.Column('nome_disciplina', db.String, nullable=True)
    conteudo = db.Column('conteudo', db.Text, nullable=False)
    nivel_importancia = db.Column('nivel_importancia', db.String(1), nullable=False)

    aluno = db.relationship('Aluno', foreign_keys=id_aluno)

    def __init__(self, id_aluno, nome, prazo_entrega, tag, disciplina, conteudo, nivel_importancia):
        self.id_aluno = id_aluno
        self.nome = nome
        self.prazo_entrega = prazo_entrega
        self.tag = tag
        self.disciplina = disciplina
        self.conteudo = conteudo
        self.nivel_importancia = nivel_importancia

    def __repr__(self):
        return '<Atividade %s>' % self.nome