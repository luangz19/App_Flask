from projeto import app, db
from flask import render_template, request, redirect, url_for
from projeto.livro import Livro

@app.route("/")
def lista_livros():
    page = request.args.get("page", 1, type=int)
    per_page = 2
    todos_livros = Livro.query.paginate(page=page, per_page=per_page)
    return render_template("livros.html", 
                           livros=todos_livros)

@app.route("/add_livro", methods=["GET", "POST"])
def adicionar_livro():
    nome = request.form.get("nome")
    descricao = request.form.get("descricao")
    valor = request.form.get("valor")

    if request.method == "POST":
        livro_add = Livro(nome, descricao, valor)
        db.session.add(livro_add)
        db.session.commit()
        return redirect(url_for("lista_livros"))
    
    return render_template("novo_livro.html")

@app.route("/<int:id>/atualiza_livro", methods=["GET", "POST"])
def atualizar_livro(id):
    # select from livro where id = 2
    livro_bd = Livro.query.filter_by(id=id).first()
    if request.method == "POST":
        nome = request.form["nome"]
        descricao = request.form["descricao"]
        valor = request.form["valor"]

        Livro.query.filter_by(id=id).update({
            "nome":nome,
            "descricao":descricao,
            "valor":valor
        })
        db.session.commit()
        return redirect(url_for("lista_livros"))
    return render_template(
        "atualiza_livro.html",
        livro=livro_bd
    )

@app.route("/<int:id>/remove_livro")
def remover_livro(id):
    livro_db = Livro.query.filter_by(id=id).first()
    db.session.delete(livro_db)
    db.session.commit()
    return redirect(url_for("lista_livros"))