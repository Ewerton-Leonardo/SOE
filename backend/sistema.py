from backend.aluno import Aluno
class Sistema:
    def __init__(self):
        self.alunos = list()
        self.professores = list()

    def cadastrarAluno(self, nome, id, senha, dataNasc, curso):
        aluno = Aluno(nome, id, senha, dataNasc, curso)
        for a in self.alunos:
            if aluno.id == a.id:
                return False
            else:
                self.alunos.append(aluno)
                return True

    def cadastrarProfessor(self, nome, id, senha, dataNasc, curso):
        aluno = Aluno(nome, id, senha, dataNasc, curso)
        for a in self.alunos:
            if aluno.id == a.id:
                return False
            else:
                self.alunos.append(aluno)
                return True