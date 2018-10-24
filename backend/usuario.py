from datetime import date


class Usuario:
	def __init__(self, nome: str, id: str, senha: str, dataNasc: date) -> None:
		self.nome = nome
		self.id = id
		self.senha = senha
		self.dataNasc = dataNasc
		self.disciplinas = list()

	def autenticaSenha(self, senha):
		if self.senha == senha:
			return True
		else:
			return False

	def fazerLogin(self):
		pass
