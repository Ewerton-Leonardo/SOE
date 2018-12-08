from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, RadioField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length
from wtforms.fields.html5 import DateField, DateTimeField, TimeField


class CadastroAlunoForm(FlaskForm):
    username = StringField('Nome de usuário', validators=[DataRequired(message='Nome de usuário obrigatório'),
                                                          Length(min=6, max=20, message='Número de caracteres do nome de usuário entre 6 e 20')])
    senha = PasswordField('Senha', validators=[DataRequired(message='Senha obrigatória'), Length(min=6, max=30)])
    nome = StringField('Nome e sobrenome', validators=[DataRequired(message='Nome e sobrenome obrigatórios')])
    data_nasc = DateField('Data de nascimento', validators=[DataRequired(message='Data de nascimento incorreta')])
    curso = StringField('Curso', validators=[DataRequired(message='Curso obrigatório')])
    enviar = SubmitField('Cadastrar-se')


class AtividadeForm(FlaskForm):
    nome = StringField('Nome da atividade', validators=[DataRequired(message=' obrigatório')])
    prazo_entrega = DateTimeField('Prazo de entrega', validators=[DataRequired(message=' obrigatório')], format='%d/%m/%Y %H:%M')
    tag = StringField('Tag')
    disciplina = SelectField('Disciplina', coerce=str)
    conteudo = TextAreaField('Conteúdo da atividade', validators=[DataRequired(message=' obrigatório')])
    nivel_importancia = RadioField('Nivel de importância', choices=[('A', 'A'), ('B', 'B'), ('C', 'C')])
    enviar = SubmitField('Adicionar atividade')


class DisciplinaForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired(message='Nome da disciplina obrigatório'),
                                           Length(min=3, max=20)])
    enviar = SubmitField('Adicionar disciplina')


class HorarioForm(FlaskForm):
    disciplina = SelectField('Disciplina', coerce=str, validators=[DataRequired()])
    professor = StringField('Nome do professor', validators=[DataRequired()])
    dia = SelectField('Dia da semana', coerce=str, choices=[('Segunda-Feira', 'Segunda-Feira'),
                                                            ('Terça-Feira', 'Terça-Feira'),
                                                            ('Quarta-Feira', 'Quarta-Feira'),
                                                            ('Quinta-Feira', 'Quinta-Feira'),
                                                            ('Sexta-Feira', 'Sexta-Feira'), ('Sábado', 'Sábado'),
                                                            ('Domingo', 'Domingo')], validators=[DataRequired()])
    hora = TimeField('Horario', format='%H:%M')
    sala = StringField('Sala', validators=[Length(max=20)])
    enviar = SubmitField('Adicionar horário')


class LoginForm(FlaskForm):
    username = StringField('Nome de usuário', validators=[DataRequired(message='Nome de usuário obrigatório'),
                                                          Length(max=20)])
    senha = PasswordField('Senha', validators=[DataRequired(message='Senha obrigatória'), Length(min=6, max=30)])
    entrar = SubmitField('Entrar')
