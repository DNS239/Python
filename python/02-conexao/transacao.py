import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "clientes.sqlite")

cursor = conexao.cursor()

cursor.row_factory = sqlite3.Row


try:
    cursor.execute(
        "INSERT INTO clientes (nome, email) VALUES (?, ?)", ("Test3", "test3@gmail.com")
    )
    #cursor.execute("DELETE FROM clientes WHERE id = 11;")

    cursor.execute(
        "INSERT INTO clientes (id, nome, email) VALUES (?, ?, ?)",
        (2, "Test4", "test4@gmail.com"),
    )
    conexao.commit()
except Exception as exc:
    print(f"Ops! um error ocorreu! {exc}")
    conexao.rollback()
