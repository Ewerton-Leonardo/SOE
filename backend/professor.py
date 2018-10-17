from backend.usuario import Usuario
from datetime import date


class Professor(Usuario):
	def __init__(self, nome: str, id: str, senha: str, dataNasc: date):
		super().__init__(nome, id, senha, dataNasc)
		self.turmas = list()
		self.horarios = list()
