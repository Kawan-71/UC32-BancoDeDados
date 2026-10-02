from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)


def conectar_banco():
    banco = sqlite3.connect("biblioteca.db")
    banco.row_factory = sqlite3.Row
    return banco


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/livros")
def livros():
    banco = conectar_banco()

    livros = banco.execute("""
        SELECT
            livros.id_livro,
            livros.titulo,
            livros.ano,
            autores.nome AS autor
        FROM livros
        LEFT JOIN autores
        ON livros.id_autor = autores.id_autor
    """).fetchall()

    banco.close()

    return render_template("livros.html", livros=livros)


@app.route("/cadastrar", methods=["GET", "POST"])
def cadastrar():

    banco = conectar_banco()

    autores = banco.execute(
        "SELECT * FROM autores"
    ).fetchall()

    if request.method == "POST":

        titulo = request.form["titulo"]
        ano = request.form["ano"]
        id_autor = request.form["id_autor"]

        banco.execute("""
            INSERT INTO livros (titulo, ano, id_autor)
            VALUES (?, ?, ?)
        """, (titulo, ano, id_autor))

        banco.commit()
        banco.close()

        return redirect("/livros")

    banco.close()

    return render_template(
        "cadastrar.html",
        autores=autores
    )


@app.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):

    banco = conectar_banco()

    autores = banco.execute(
        "SELECT * FROM autores"
    ).fetchall()

    if request.method == "POST":

        titulo = request.form["titulo"]
        ano = request.form["ano"]
        id_autor = request.form["id_autor"]

        banco.execute("""
            UPDATE livros
            SET titulo = ?, ano = ?, id_autor = ?
            WHERE id_livro = ?
        """, (titulo, ano, id_autor, id))

        banco.commit()
        banco.close()

        return redirect("/livros")

    livro = banco.execute(
        "SELECT * FROM livros WHERE id_livro = ?",
        (id,)
    ).fetchone()

    banco.close()

    return render_template(
        "editar.html",
        livro=livro,
        autores=autores
    )


@app.route("/excluir/<int:id>")
def excluir(id):

    banco = conectar_banco()

    banco.execute(
        "DELETE FROM livros WHERE id_livro = ?",
        (id,)
    )

    banco.commit()
    banco.close()

    return redirect("/livros")


if __name__ == "__main__":
    app.run(debug=True)