from flask import Flask, render_template, request, redirect, url_for
from db import *
import logging

app = Flask(__name__)
a = Atleta
t = Time
arb = Arbitro
c = Competição

@app.route('/')
def listar_atletas():
    atletas = a.listar_atleta()
    return render_template("volei.html", atletas=atletas)

@app.route("/remover/<int:chave>")
def apagar(chave):
    a.remove_atleta(chave)
    return redirect(url_for('listar_atletas'))

@app.route("/novo", methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        dados = request.form.to_dict()
        a.novo_atleta(dados.get('nome'), dados.get('posicao'), dados.get('altura'))
        return redirect(url_for('listar_atletas'))
    return render_template('form_volei.html', atleta=None, title='Novo Atleta')

@app.route("/editar/<int:chave>", methods=['GET', 'POST'])
def editar(chave):
    if request.method == 'POST':
        dados = request.form.to_dict()
        a.atualiza_atleta(chave, dados.get('nome'), dados.get('posicao'), dados.get('altura'))
        return redirect(url_for('listar_atletas'))
    atleta = a.detalha_atleta(chave)
    return render_template('form_volei.html', atleta=atleta, title='Editar Atleta')

@app.route('/times', methods=['GET'])
def listar_times():
    times = t.listar_time()
    return render_template("time.html", times=times)

@app.route("/novo_time", methods=['GET', 'POST'])
def cadastrar_time():
    if request.method == 'POST':
        dados = request.form.to_dict()
        t.novo_time(dados.get('nome'))
        return redirect(url_for('listar_times'))
    return render_template('form_time.html', time=None, title='Novo Time')

@app.route("/editar_time/<int:chave>", methods=['GET', 'POST'])
def editar_time(chave):
    if request.method == 'POST':
        dados = request.form.to_dict()
        t.atualiza_time(chave, dados.get('nome'))
        return redirect(url_for('listar_times'))
    times = t.detalha_time(chave)
    return render_template('form_time.html', time=times, title='Editar Time')

@app.route("/remover_time/<int:chave>")
def apagar_time(chave):
    t.remove_time(chave)
    return redirect(url_for('listar_times'))

@app.route('/arbitro', methods=['GET'])
def listar_arbitro():
    arbitro = arb.listar_arbitro()
    return render_template("arbitro.html", arbitro=arbitro)

@app.route("/novo_arbitro", methods=['GET', 'POST'])
def cadastrar_arbitro():
    if request.method == 'POST':
        dados = request.form.to_dict()
        arb.novo_arbitro(dados.get('nome'), dados.get('documento'))
        return redirect(url_for('listar_arbitro'))
    return render_template('form_arbitro.html', arbitro=None, title='Novo Arbitro')

@app.route("/editar_arbitro/<int:chave>", methods=['GET', 'POST'])
def editar_arbitro(chave):
    if request.method == 'POST':
        dados = request.form.to_dict()
        arb.atualiza_arbitro(chave, dados.get('nome'), dados.get('documento'))
        return redirect(url_for('listar_arbitro'))
    arbitro = arb.detalha_arbitro(chave)
    return render_template('form_arbitro.html', arbitro=arbitro, title='Editar Arbitro')

@app.route("/remover_arbitro/<int:chave>")
def apagar_arbitro(chave):
    arb.remove_arbitro(chave)
    return redirect(url_for('listar_arbitro'))

@app.route('/competicao', methods=['GET'])
def listar_competicao():
    competicao = c.listar_competicao()
    return render_template("competicao.html", competicao=competicao)

@app.route("/novo_competicao", methods=['GET', 'POST'])
def cadastrar_competicao():
    if request.method == 'POST':
        dados = request.form.to_dict()
        c.novo_competicao(dados.get('nome'))
        return redirect(url_for('listar_competicao'))
    return render_template('form_competicao.html', competicao=None, title='Nova Competição')

@app.route("/editar_competicao/<int:chave>", methods=['GET', 'POST'])
def editar_competicao(chave):
    if request.method == 'POST':
        dados = request.form.to_dict()
        c.atualiza_competicao(chave, dados.get('nome'))
        return redirect(url_for('listar_competicao'))
    competicao = c.detalha_competicao(chave)
    return render_template('form_competicao.html', competicao=competicao, title='Editar Competição')

@app.route("/remover_competicao/<int:chave>")
def apagar_competicao(chave):
    c.remove_competicao(chave)
    return redirect(url_for('listar_competicao'))

# Nicolas imoral de fácil, nós que pensavamos demais, debug ajuda muito
if __name__ == '__main__':
    app.run(debug=False)
