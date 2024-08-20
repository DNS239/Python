import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "clientes.sqlite")

cursor = conexao.cursor()

cursor.row_factory = sqlite3.Row


id_client = input("Inform o Id do client:")
cursor.execute("SELECT * FROM clientes WHERE id=?", (id_client,))
#cursor.execute(f"SELECT * FROM clientes WHERE id={id_client}")

clients = cursor.fetchall()

for cliente in clients:
    print(dict(cliente))