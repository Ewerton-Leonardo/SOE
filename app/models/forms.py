from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, TextAreaField, IntegerField, RadioField, SubmitField, DateField, DateTimeField
from wtforms.validators import DataRequired, Length, EqualTo
# from wtforms.fields.html5 import DateField


class CadastroAlunoForm(FlaskForm):
    username = StringField('Nome de usuário', validators=[DataRequired(message='Nome de usuário obrigatório'), 
                            Length(min=6, max=20, message='Número de caracteres do nome de usuário entre 6 e 20')])
    senha = PasswordField('Senha', validators=[DataRequired(message='Senha obrigatória'), 
                           Length(min=6, max=30)])
    nome = StringField('Nome e sobrenome', validators=[DataRequired(message='Nome e sobrenome obrigatórios')])
    data_nasc = DateField('Data de nascimento', validators=[DataRequired(message='Data de nascimento incorreta')], 
                           format='%d/%m/%Y')
    curso = StringField('Curso', validators=[DataRequired(message='Curso obrigatório')])
    enviar = SubmitField('Cadastrar-se')


class CadastroProfessorForm(FlaskForm):
    username = StringField('Nome de usuário', validators=[DataRequired('Nome de usuário obrigatório'), 
                            Length(min=6, max=20)])
    senha = PasswordField('Senha', validators=[DataRequired(message='Senha obrigatória'), Length(min=6, max=30)])
    nome = StringField('Nome e sobrenome', validators=[DataRequired('Nome e sobrenome obrigatórios')])
    data_nasc = DateField('Data de nascimento', validators=[DataRequired(message='Data de nascimento obrigatória')], 
                           format='%d/%m/%Y')
    enviar = SubmitField('Cadastrar-se')


class NovaAtividadeForm(FlaskForm):
    nome = StringField('Nome da atividade', validators=[DataRequired(message=' obrigatório')])
    prazo_entrega = DateTimeField('Prazo de entrega', validators=[DataRequired(message=' obrigatório')], format='%d/%m/%Y %H:%M')
    tag = StringField('Tag')
    nome_disciplina = StringField('Nome da disciplina')
    conteudo = TextAreaField('Conteúdo da atividade', validators=[DataRequired(message=' obrigatório')])
    nivel_importancia = RadioField('Nivel de importância', choices=[('A', 'A'), ('B', 'B'), ('C', 'C')])
    enviar = SubmitField('Adicionar atividade')


class NovaDisciplinaForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired(message='Nome da disciplina obrigatório'), Length(min=3, max=20)])
    enviar = SubmitField('Cadastrar disciplina')


class NovoHorarioForm(FlaskForm):
    pass


class LoginForm(FlaskForm):
    username = StringField('Nome de usuário', validators=[DataRequired(message='Nome de usuário obrigatório'), Length(max=20)])
    senha = PasswordField('Senha', validators=[DataRequired(message='Senha obrigatória'), Length(min=6, max=30)])
    entrar = SubmitField('Entrar')
