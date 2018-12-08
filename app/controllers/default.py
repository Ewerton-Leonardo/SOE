from app import app
from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, login_required, current_user
from app import db

from app.models.forms import LoginForm, CadastroAlunoForm
from app.models.aluno import Aluno
from app.models.atividade import Atividade
from app.models.disciplina import Disciplina
from app.models.horario import Horario

from app.models.forms import AtividadeForm, DisciplinaForm, HorarioForm


@app.route('/')
@app.route('/index')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('pagina_inicial'))
    return render_template('index.html')


@app.route('/login', methods=['get', 'post'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('pagina_inicial'))
    form = LoginForm(request.form)
    title_form = "Login"
    if form.is_submitted():
        aluno = Aluno.query.filter_by(username=form.username.data).first()
        if aluno and aluno.senha == form.senha.data:
            login_user(aluno)
            flash("Logado", 'sucesso')
            return redirect(url_for('pagina_inicial'))
        else:
            flash("Login inválido, ")
    return render_template('login.html', form=form, title_form=title_form)


@app.route('/cadastro_aluno', methods=['get', 'post'])
def cadastro_aluno():
    if current_user.is_authenticated:
        return redirect(url_for('pagina_inicial'))
    form = CadastroAlunoForm(request.form)
    title_form = "Cadastro"
    if request.method == 'POST' and form.validate_on_submit():
        existe_aluno = Aluno.query.filter_by(username=form.username.data).first()
        if not existe_aluno:
            aluno = Aluno(form.username.data, form.senha.data, form.nome.data, form.data_nasc.data, form.curso.data)
            flash('Aluno cadastrado', 'sucesso')
            db.session.add(aluno)
            db.session.commit()
            return redirect(url_for('index'))
        else:
            flash('Nome de usuário já cadastrado')
    elif form.errors != {} and form.is_submitted():
        for index_erro in form.errors:
            flash(form.errors[index_erro][0], 'erro')
    for index_erro in form.errors:
        flash(form.errors[index_erro][0], 'erro')
    return render_template('cadastro_aluno.html', form=form, title_form=title_form)


@app.route('/pagina_inicial')
@login_required
def pagina_inicial():
    return render_template('templates_aluno/pagina_inicial.html')


@app.route('/atividades')
@login_required
def atividades():
    list_atividades = Atividade.query.filter_by(id_aluno=current_user.id).all()
    return render_template('templates_aluno/atividades.html', list_atividades=list_atividades)


@app.route('/atividades/adicionar_atividade', methods=['get', 'post'])
@login_required
def adicionar_atividade():
    form = AtividadeForm(request.form)
    form.disciplina.choices = [(row.nome, row.nome)
                               for row in Disciplina.query.filter_by(id_aluno=current_user.id).all()]
    title_form = "Adicionar Atividade"
    if request.method == 'POST' and form.validate_on_submit():
        atividade = Atividade(current_user.id, form.nome.data, form.prazo_entrega.data, form.tag.data, form.disciplina.data, form.conteudo.data, form.nivel_importancia.data)
        db.session.add(atividade)
        db.session.commit()
        flash('Atividade adicionada com sucesso!', 'sucesso')
        return redirect(url_for('atividades'))
    elif form.errors != {} and form.is_submitted():
        for index_erro in form.errors:
            flash(index_erro + form.errors[index_erro][0], 'erro')
    return render_template('templates_aluno/adicionar_atividade.html', form=form, title_form=title_form)


@app.route('/atividades/visualizar_atividade/<int:id_atividade>')
@login_required
def visualizar_atividade(id_atividade):
    atividade = Atividade.query.filter_by(id=id_atividade, id_aluno=current_user.id).first()
    return render_template('templates_aluno/visualizar_atividade.html', atividade=atividade)


@app.route('/atividades/editar_atividade/<int:id_atividade>', methods=['get', 'post'])
@login_required
def editar_atividade(id_atividade):
    form = AtividadeForm(request.form)
    title_form = "Editar Atividade"
    atividade = Atividade.query.filter_by(id=id_atividade, id_aluno=current_user.id).first()
    if atividade is not None:
        form.disciplina.choices = [(str(row.id), row.nome) for row in Disciplina.query.filter_by(id_aluno=current_user.id).all()]
        form.nome.data = atividade.nome
        form.prazo_entrega.data = atividade.prazo_entrega
        form.tag.data = atividade.tag
        form.disciplina.data = atividade.nome_disciplina
        form.conteudo.data = atividade.conteudo
        form.nivel_importancia.data = atividade.nivel_importancia
    else:
        flash('Atividade não encontrada', 'erro')
        return redirect(url_for('atividades'))
    if request.method == 'POST' and form.validate_on_submit():
        atividade.nome = request.form.get('nome')
        atividade.prazo_entrega = request.form.get('prazo_entrega')
        atividade.tag = request.form.get('tag')
        atividade.nome_disciplina = request.form.get('disciplina')
        flash(request.form.get('disciplina'), 'erro')
        atividade.conteudo = request.form.get('conteudo')
        atividade.nivel_importancia = request.form.get('nivel_importancia')
        db.session.add(atividade)
        db.session.commit()
        flash('Atividade editada com sucesso!', 'sucesso')
        return redirect(url_for('atividades'))
    elif form.errors != {} and form.is_submitted():
        for index_erro in form.errors:
            flash(form.errors[index_erro][0], 'erro')
    return render_template('templates_aluno/editar_atividade.html', form=form, title_form=title_form)


@app.route('/atividades/apagar_atividade/<int:id_atividade>')
@login_required
def apagar_atividade(id_atividade):
    atividade = Atividade.query.filter_by(id=id_atividade, id_aluno=current_user.id).first()
    db.session.delete(atividade)
    db.session.commit()
    flash('Atividade apagada com sucesso!', 'sucesso')
    return redirect(url_for('atividades'))


@app.route('/disciplinas')
@login_required
def disciplinas():
    list_disciplinas = Disciplina.query.filter_by(id_aluno=current_user.id).all()
    return render_template('templates_aluno/disciplinas.html', list_disciplinas=list_disciplinas)


@app.route('/disciplinas/adicionar_disciplina', methods=['get', 'post'])
@login_required
def adicionar_disciplina():
    form = DisciplinaForm(request.form)
    title_form = "Adicionar Disciplina"
    if request.method == 'POST' and form.validate_on_submit():
        disciplina = Disciplina(current_user.id, form.nome.data)
        db.session.add(disciplina)
        db.session.commit()
        flash('Disciplina adicionada com sucesso!', 'sucesso')
        return redirect(url_for('disciplinas'))
    elif form.errors == {} and form.is_submitted():
        for index_erro in form.errors:
            flash(form.errors[index_erro][0], 'erro')
    return render_template('templates_aluno/adicionar_disciplina.html', form=form, title_form=title_form)


@app.route('/disciplinas/editar_disciplina/<int:id_disciplina>', methods=['get', 'post'])
@login_required
def editar_disciplina(id_disciplina):
    form = DisciplinaForm(request.form)
    title_form = "Editar Disciplina"
    disciplina = Disciplina.query.filter_by(id=id_disciplina, id_aluno=current_user.id).first()
    if disciplina is not None:
        form.nome.data = disciplina.nome
    else:
        flash('Disciplina não encontrada', 'erro')
        return redirect(url_for('disciplinas'))
    if request.method == 'POST' and form.validate_on_submit():
        disciplina.nome = request.form.get('nome')
        db.session.commit()
        flash('Disciplina editada com sucesso!', 'sucesso')
        return redirect(url_for('disciplinas'))
    elif form.errors == {} and form.is_submitted():
        for index_erro in form.errors:
            flash(form.errors[index_erro][0], 'erro')
    return render_template('templates_aluno/editar_disciplina.html', form=form, title_form=title_form)


@app.route('/disciplinas/apagar_disciplina/<int:id_disciplina>')
@login_required
def apagar_disciplina(id_disciplina):
    disciplina = Disciplina.query.filter_by(id=id_disciplina, id_aluno=current_user.id).first()
    db.session.delete(disciplina)
    db.session.commit()
    flash('Disciplina apagada com sucesso!', 'sucesso')
    return redirect(url_for('disciplinas'))


@app.route('/horarios')
@login_required
def horarios():
    list_horarios = Horario.query.filter_by(id_aluno=current_user.id).order_by('hora').all()
    return render_template('templates_aluno/horarios.html', list_horarios=list_horarios)


@app.route('/horarios/adicionar_horario', methods=['get', 'post'])
@login_required
def adicionar_horario():
    form = HorarioForm(request.form)
    form.disciplina.choices = [(row.nome, row.nome)
                               for row in Disciplina.query.filter_by(id_aluno=current_user.id).all()]
    title_form = "Adicionar Horário"
    if request.method == 'POST' and form.validate_on_submit():
        horario = Horario(current_user.id, form.disciplina.data, form.professor.data, form.dia.data, form.hora.data, form.sala.data)
        db.session.add(horario)
        db.session.commit()
        flash('Horário adicionado com sucesso!', 'sucesso')
        return redirect(url_for('horarios'))
    elif form.errors == {} and form.is_submitted():
        for index_erro in form.errors:
            flash(form.errors[index_erro][0], 'erro')
    return render_template('templates_aluno/adicionar_horario.html', form=form, title_form=title_form)


@app.route('/horarios/editar_horario/<int:id_horario>', methods=['get', 'post'])
@login_required
def editar_horario(id_horario):
    form = HorarioForm(request.form)
    title_form = "Editar Horário"
    horario = Horario.query.filter_by(id=id_horario, id_aluno=current_user.id).first()
    if horario is not None:
        form.disciplina.choices = [(row.nome, row.nome)
                                   for row in Disciplina.query.filter_by(id_aluno=current_user.id).all()]
        form.disciplina.data = horario.disciplina
        form.professor.data = horario.professor
        form.dia.data = horario.dia
        form.hora.data = horario.hora
        form.sala.data = horario.sala
        if request.method == 'POST' and form.validate_on_submit():
            horario.disciplina = request.form.get('disciplina')
            horario.professor = request.form.get('professor')
            horario.dia = request.form.get('dia')
            horario.hora = request.form.get('hora')
            horario.sala = request.form.get('sala')
            db.session.commit()
            flash('Horário editado com sucesso!', 'sucesso')
            return redirect(url_for('horarios'))
        elif form.errors == {} and form.is_submitted():
            for index_erro in form.errors:
                flash(form.errors[index_erro][0], 'erro')
    else:
        flash('Horário não encontrado', 'erro')
        return redirect(url_for('horarios'))

    return render_template('templates_aluno/editar_horario.html', form=form, title_form=title_form)


@app.route('/horarios/apagar_horario/<int:id_horario>')
@login_required
def apagar_horario(id_horario):
    horario = Horario.query.filter_by(id=id_horario, id_aluno=current_user.id).first()
    db.session.delete(horario)
    db.session.commit()
    flash('Horário apagado com sucesso!', 'sucesso')
    return redirect(url_for('horarios'))


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Você foi deslogado')
    return redirect(url_for('index'))






