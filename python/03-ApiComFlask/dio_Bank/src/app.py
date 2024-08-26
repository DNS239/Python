from flask import Flask, url_for, request

app = Flask(__name__)


@app.route("/olaMundo/<usuario>/<int:idade>/<float:altura>")
def hello_world(usuario, idade, altura):
    # print(idade)
    # print(f"tipo da variavel idade: {type(idade)}")
    # print(f"tipo da variavel usuario: {type(usuario)}")
    # print(f"tipo da variavel altura: {type(altura)}")
    return {
        'Usuario': usuario,
        'Idade': idade,
        'Altura': altura,
    }


@app.route("/bemVindo")
def bem_Vindo():
    return {"message": "Óla, mundo"}


@app.route("/projects/")
def projects():
    return "The project page"


@app.route("/about", methods=["GET", "POST"])
def about():
    if request.method == "GET":
        return "This is a GET"
    else:
        return "This is a POST"


with app.test_request_context():
    print(url_for("bem_Vindo"))
    print(url_for("projects"))
    print(url_for("about", next="/"))
    print(url_for("hello_world", usuario="Dns", idade=28, altura=1.68))
