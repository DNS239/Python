from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",
        DATABASE="diobanck.sqlite",
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # # ensure the instance folder exists
    # try:
    #     os.makedirs(app.instance_path)
    # except OSError:
    #     pass

    from . import db

    db.init_app(app)

    return app


# from flask import Flask, url_for, request

# app = Flask(__name__)


# @app.route("/olaMundo/<usuario>/<int:idade>/<float:altura>")
# def hello_world(usuario, idade, altura):
#     # print(idade)
#     # print(f"tipo da variavel idade: {type(idade)}")
#     # print(f"tipo da variavel usuario: {type(usuario)}")
#     # print(f"tipo da variavel altura: {type(altura)}")
#     return {
#         'Usuario': usuario,
#         'Idade': idade,
#         'Altura': altura,
#     }


# @app.route("/bemVindo")
# def bem_Vindo():
#     return {"message": "Óla, mundo"}


# @app.route("/projects/")
# def projects():
#     return "The project page"


# @app.route("/about", methods=["GET", "POST"])
# def about():
#     if request.method == "GET":
#         return "This is a GET"
#     else:
#         return "This is a POST"


# with app.test_request_context():
#     print(url_for("bem_Vindo"))
#     print(url_for("projects"))
#     print(url_for("about", next="/"))
#     print(url_for("hello_world", usuario="Dns", idade=28, altura=1.68))
