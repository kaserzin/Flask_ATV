from flask import *
from db import Atleta, Time, Competicao

app = Flask(__name__)
a = Atleta
t = Time
c = Competicao

@app.route('/')
def list_boardgames():
    atletas = a.listar_atleta()
    return render_template("volei.html", atletas=atletas)

@app.route("/remover/<int:chave>")
def apagar(chave):
    a.remove_atleta(chave)
    return redirect('/')

@app.route("/novo", methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        dados = request.form.to_dict()
        a.novo_atleta(dados.get('nome'), dados.get('posicao'), int(dados.get('altura')))
        return redirect('/')
    return render_template('form_volei.html', atleta=None, title='Novo Atleta')

@app.route("/editar/<int:chave>", methods=['GET', 'POST'])
def editar(chave):
    if request.method == 'POST':
        dados = request.form.to_dict()
        a.atualiza_atleta(chave, dados.get('nome'), dados.get('posicao'), int(dados.get('altura')))
        return redirect('/')
    atleta = a.detalha_atleta(chave)
    if atleta is None:
        flash('Atleta não encontrado')
        return redirect('/')
    return render_template('form_volei.html', atleta=atleta, title='Editar Atleta')

@app.route('/times')
def list_times():
    times = t.listar_times()
    return render_template("times.html", times=times)

@app.route("/times/remover/<int:id_time>")
def apagar_time(id_time):
    t.remove_time(id_time)
    return redirect('/times')

@app.route("/times/novo", methods=['GET', 'POST'])
def cadastrar_time():
    if request.method == 'POST':
        dados = request.form.to_dict()
        t.novo_time(dados.get('nome'))
        return redirect('/times')
    return render_template('form_times.html', time=None, title='Novo Time')

@app.route("/times/editar/<int:id_time>", methods=['GET', 'POST'])
def editar_time(id_time):
    if request.method == 'POST':
        dados = request.form.to_dict()
        t.atualiza_time(id_time, dados.get('nome'))
        return redirect('/times')
    time = t.detalha_time(id_time)
    return render_template('form_times.html', time=time, title='Editar Time')

@app.route('/competicoes')
def list_competicoes():
    competicoes = c.listar_competicoes()
    return render_template("competicoes.html", competicoes=competicoes)

@app.route("/competicoes/remover/<int:id_competicao>")
def apagar_competicao(id_competicao):
    c.remove_competicao(id_competicao)
    return redirect('/competicoes')

@app.route("/competicoes/novo", methods=['GET', 'POST'])
def cadastrar_competicao():
    if request.method == 'POST':
        dados = request.form.to_dict()
        c.nova_competicao(dados.get('nome'))
        return redirect('/competicoes')
    return render_template('form_competicoes.html', competicao=None, title='Nova Competição')

@app.route("/competicoes/editar/<int:id_competicao>", methods=['GET', 'POST'])
def editar_competicao(id_competicao):
    if request.method == 'POST':
        dados = request.form.to_dict()
        c.atualiza_competicao(id_competicao, dados.get('nome'))
        return redirect('/competicoes')
    competicao = c.detalha_competicao(id_competicao)
    return render_template('form_competicoes.html', competicao=competicao, title='Editar Competição')


if __name__ == '__main__':
    app.run()
    