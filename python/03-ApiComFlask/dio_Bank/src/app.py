import os
from datetime import datetime

import click
import sqlalchemy as sa
from flask import Flask, current_app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column





class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


class User(db.Model):
    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True)
    username: Mapped[str] = mapped_column(sa.String, unique=True, nullable=False)
    #email: Mapped[str] = mapped_column(sa.String)


    def __repr__(self) -> str:
        return f"User(id={self.id!r}, username={self.username!r})"
    
    
class Post(db.Model):
    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True)
    title: Mapped[str] = mapped_column(sa.String, nullable=False)
    body: Mapped[str] = mapped_column(sa.String, nullable=False)
    created: Mapped[datetime] = mapped_column(sa.DateTime, server_default=sa.func.now())
    author_id: Mapped[int] = mapped_column(sa.ForeignKey('user.id'))


    def __repr__(self) -> str:
        return f"Post(id={self.id!r}, title={self.title!r}, author_id={self.author_id!r})"

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
        SQLALCHEMY_DATABASE_URI="sqlite:///dio_bank.sqlite",
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # register cli commands
    app.cli.add_command(init_db_command)

    # initialize extensions
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
