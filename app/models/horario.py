from app import db


class Horario(db.Model):
    __tablename__ = 'horario'

    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    id_aluno = db.Column('id_aluno', db.Integer, db.ForeignKey('aluno.id'), nullable=False)
    disciplina = db.Column('disciplina', db.String, nullable=False)
    professor = db.Column('professor', db.String, nullable=False)
    dia = db.Column('dia', db.String(15), nullable=False)
    hora = db.Column('hora', db.Time, nullable=True)
    sala = db.Column('sala', db.String(20), nullable=True)

    aluno = db.relationship('Aluno', foreign_keys=id_aluno)

    def __init__(self, id_aluno, disciplina, professor, dia, hora, sala):
        self.id_aluno = id_aluno
        self.disciplina = disciplina
        self.professor = professor
        self.dia = dia
        self.hora = hora
        self.sala = sala

