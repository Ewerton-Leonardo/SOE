from backend.aluno import Aluno
from backend.professor import Professor
from backend.atividade import Atividade
from datetime import date
from random import choice

class Sistema:
    def __init__(self):
        self.alunos = list()
        self.professores = list()
        self.usuarios = list()


    def cadastrarAluno(self, nome, id, senha, dataNasc, curso):
        aluno = Aluno(nome, id, senha, dataNasc, curso)
        if aluno.id in self.usuarios:
            return False
        else:
            self.alunos.append(aluno)
            self.usuarios.append({'id': aluno.id, 'senha': aluno.senha, 'tipo': 'Aluno'})
            return True

    def cadastrarProfessor(self, nome, id, senha, dataNasc):
        prof = Professor(nome, id, senha, dataNasc)
        if prof.id in self.professores:
            return False
        else:
            self.professores.append(prof)
            self.usuarios.append({'id': prof.id, 'senha': prof.senha, 'tipo': 'Professor'})
            return True


    def login(self, id, senha):
        for u in self.usuarios:
            if u['id'] == id:
                if u['senha'] == senha:
                    if u['tipo'] == 'Professor':
                        for prof in self.professores:
                            if prof.id == u['id']:
                                self.menuProfessor(prof)
                    elif u['tipo'] == 'Aluno':
                        for aluno in self.alunos:
                            if aluno.id == u['id']:
                                self.menuAluno(aluno)
                else:
                    return False
            else:
                return False

    def gerarID(self, tamanho):
        caracters = 'abcdefghijklmnopqrstuvwxyz'
        list = []
        id = ''
        while len(list) < (len(caracters) ** tamanho):
            for c in range(tamanho):
                id += choice(caracters)
        return id

    def inserirNovaAtividade(self, nome, prazoEntrega, tag, disciplina, conteudo, nivelImportancia, user):
        id = self.gerarID(4)
        while id in user.atividades:
            id = self.gerarID(4)
        atividade = Atividade(nome, id, prazoEntrega, tag, disciplina, conteudo, nivelImportancia)
        user.atividades.append(atividade)


    def menuPrincipal(self):
        print('SOE')
        print('Menu Inicial')
        print('1 - Cadastrar aluno')
        print('2 - Cadastrar professor')
        print('3 - Fazer login')
        print('x - Sair')
        opcao = input('Digite a opção:').lower()

        while opcao != 'x':

            if opcao == '1':
                nome = input('Nome: ')
                id = input('ID: ')
                senha = input('Senha: ')
                dataNasc = input('Data de Nascimento: ')
                dia, mes, ano = dataNasc.split('/')
                dataNasc = date(day=int(dia), month=int(mes), year=int(ano))
                curso = input('Curso: ')
                if self.cadastrarAluno(nome, id, senha, dataNasc, curso):
                    print('Você foi cadastrado')
                else:
                    print('ID do aluno já existe')


            if opcao == '2':
                nome = input('Nome: ')
                id = input('ID: ')
                senha = input('Senha: ')
                dataNasc = input('Data de Nascimento: ')
                dia, mes, ano = dataNasc.split('/')
                dataNasc = date(day=int(dia), month=int(mes), year=int(ano))
                if self.cadastrarProfessor(nome, id, senha, dataNasc):
                    print('Você foi cadastrado')
                else:
                    print('ID do professor já existe')


            if opcao == '3':
                id = input('ID: ')
                senha = input('Senha: ')
                self.login(id, senha)

            print('')
            print('Menu Inicial')
            print('1 - Cadastrar aluno')
            print('2 - Cadastrar professor')
            print('3 - Fazer login')
            print('x - Sair')
            opcao = input('Digite a opção:').lower()

        return opcao

    def menuAluno(self, user):
        print('')
        print('SOE')
        print('Menu Inicial - Aluno')
        print('1 - Inserir nova atividade')
        print('2 - Cadastrar disciplina')
        print('x - Sair')
        opcao = input('Digite a opção:').lower()

        while opcao != 'x':

            if opcao == '1':
                nome = input('Nome da atividade: ')
                prazoEntrega = input('Prazo de entrega (Data): ')
                tag = input('Tag: ')
                disciplina = input('Disciplina: ')
                conteudo = input('Conteudo: ')
                nivelImportancia = input('Nível importância (A, B ou C').lower()
                self.inserirNovaAtividade(nome,prazoEntrega,tag,disciplina,conteudo,nivelImportancia, user)




            print('')
            print('SOE')
            print('Menu Inicial - Aluno')
            print('1 - Inserir nova atividade')
            print('2 - Cadastrar disciplina')
            print('x - Sair')
            opcao = input('Digite a opção:').lower()
        return opcao

    def menuProfessor(self, user):
        print('SOE')
        print('Menu Inicial - Professor')
        print('1 - Cadastrar aluno')
        print('2 - Cadastrar professor')
        print('3 - Fazer login')
        print('x - Sair')
        opcao = input('Digite a opção:').lower()

        while opcao != 'x':
            print('############################')
            print('SOE')
            print('Menu Inicial - Professor')
            print('1 - Cadastrar usuário')
            print('2 - Fazer login')
            print('x - Sair')
            opcao = input('Digite a opção: ').lower()
        return opcao


app = Sistema()
app.menuPrincipal()
