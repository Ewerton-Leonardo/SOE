from backend.usuario import Usuario
from backend.atividade import Atividade
from backend.disciplina import Disciplina
from datetime import date

class Aluno(Usuario):
	def __init__(self, nome: str, id: str, senha: str, dataNasc: date, curso: str):
		super().__init__(nome, id, senha, dataNasc)
		self.atividades = list()
		self.curso = curso

	def criarAtividade(self, atividade: Atividade):
		self.atividades.append(atividade)

	def novaDisciplina(self, disciplina: Disciplina):
		self.disciplinas.append(disciplina)
