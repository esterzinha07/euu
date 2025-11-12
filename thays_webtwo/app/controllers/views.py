from app import app, db
from flask import render_template, redirect, url_for, request
from app.models.produtos import produtos

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/produtos', methods=['GET'])
def listar_produtos():
    produtos = produtos.query.all() 
    return render_template("produtos.html", produtos=produtos)

@app.route('/adicionar', methods=['POST'])
def adicionar():
    novo_produto = request.form.get('nome')

@app.route('/editar/<id>', methods=['GET', 'POST'])
def listar_usuarios():
    editar_produtos = produtos.query.all() 
    return render_template("produtos.html", editar_produtos=produtos)


    if nome and idade:
        novo = Usuario(nome=nome, idade=int(idade))
        db.session.add(novo)
        db.session.commit()

    return redirect(url_for('listar_usuarios'))