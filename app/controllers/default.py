from app import app
from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user

from app.models.forms import LoginForm, CadastroAlunoForm, CadastroProfessorForm, NovaDisciplinaForm
from app.models.tables import *

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/login', methods=['get', 'post'])
def login():
    print('aqui')
    form = LoginForm()
    flash(form.errors)
    if form.validate_on_submit():
        print('veio aqui')
        aluno = Aluno.query.filter_by(username=form.username.data).first()
        professor = Professor.query.filter_by(username=form.username.data).first()
        if aluno and aluno.senha == form.senha.data:
            login_user(aluno)
            flash("Logado")
        elif professor and professor.senha == form.senha.data:
            login_user(professor)
            flash("Logado")
        else:
            flash("Login inválido")
    return render_template('login.html', form_login=form)


@app.route('/cadastro-aluno', methods=['get', 'post'])
def cadastro_aluno():
    form = CadastroAlunoForm(request.form)
    for a in form.errors:
        flash(form.errors[a][0])
    if request.method == 'POST' and form.validate_on_submit():
        existe_aluno = Aluno.query.filter_by(username=form.username.data).first()
        if not existe_aluno:
            aluno = Aluno(form.username.data, form.senha.data, form.nome.data, form.data_nasc.data, form.curso.data)
            db.session.add(aluno)
            db.session.commit()
            aluno_cadastrado = Aluno.query.filter_by(username=aluno.username).first()
            if aluno_cadastrado:
                flash('Usuário cadastrado')
                return redirect(url_for('index'))
        else:
            flash('Nome de usuário já cadastrado')
    return render_template('cadastro-aluno.html', form=form)


@app.route('/cadastro-professor', methods=['get', 'post'])
def cadastro_professor():
    form = CadastroProfessorForm()
    if form.validate_on_submit():
        existe_professor = Professor.query.filter_by(username=form.username.data).first()
        if not existe_professor:
            professor = Professor(form.username.data, form.senha.data, form.nome.data, form.data_nasc.data)
            db.session.add(professor)
            db.session.commit()
    return render_template('cadastro-professor.html', form_cadastro_professor=form)
