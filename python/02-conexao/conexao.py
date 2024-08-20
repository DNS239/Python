import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "clientes.sqlite")

cursor = conexao.cursor()

cursor.row_factory = sqlite3.Row


def create_table(cursor):
    cursor.execute(
        "CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))"
    )
    conexao.commit()


def insert_registry(conexao, cursor, nome, email):
    data = (nome, email)
    cursor.execute("INSERT INTO clientes (nome, email) VALUES (?,?);", data)
    conexao.commit()


def update_registry(conexao, cursor, nome, email, id):
    data = (nome, email, id)
    cursor.execute("UPDATE clientes SET nome=?, email=? WHERE id=?;", data)
    conexao.commit()


def delete_registry(conexao, cursor, id):
    data = (id,)
    cursor.execute("DELETE FROM clientes WHERE id=?;", data)
    conexao.commit()


def insert_many(conexao, cursor, dados):
    cursor.executemany("INSERT INTO clientes (nome, email) VALUES (?,?);", dados)
    conexao.commit()


def recuperate_cliente(cursor, id):
    cursor.execute("SELECT * FROM clientes WHERE id=?", (id,))
    return cursor.fetchone()


def list_clientes(cursor):
    return cursor.execute("SELECT * FROM clientes ORDER BY nome;")


clientes = list_clientes(
    cursor,
)
for cliente in clientes:
    print(dict(cliente))

cliente = recuperate_cliente(cursor, 5)
print(dict(cliente))

# dados = [
#     ("Stephen Vincent Strange", "DoctorStrange@gmail.com"),
#     ("Tony Sterco", "TonySterco@gmail.com"),
#     ("Bruce Wayne", "Batman@gmail.com"),
#     ("Tony Stark", "TonyStark@gmail.com"),
#     ("Bruce Bener", "Hulk@gmail.com"),

# ]

# insert_many(conexao, cursor, dados)
# delete_registry(conexao, cursor, 2)
# update_registry(conexao, cursor, "Denis2", "Dnsss@gmail.com", 1)
