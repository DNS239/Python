import os

from flask import Flask, current_app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
import click


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


@click.command("init-db")
def init_db_command():
    """Clear the existing data and create new tables."""
    global db
    with current_app.app_context():
        db.create_all()
    click.echo("Initialized the database.")


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
    SECRET_KEY="dev",
    SQLALCHEMY_DATABASE_URI=f"sqlite:///{os.path.abspath(os.path.join(os.getcwd(), 'Dio_Bank.sqlite'))}"
)


    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    app.cli.add_command(init_db_command)
    db.init_app(app)

    # a simple page that says hello
    @app.route("/hello")
    def hello():
        return "Hello, World!"

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
