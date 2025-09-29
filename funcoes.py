import sqlite3
def cadastrar_livro(título,autor,ano):
    conn = sqlite3.connect("Biblioteca.db")
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO Biblioteca (título, autor, ano, disponivel)
    VALUES (?, ?, ?, ?)
    """, (título, autor, ano, "Sim")
    )
    conn.commit()
    conn.close()
def listar_livro():
    conexao = sqlite3.connect("Biblioteca.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM Biblioteca")

    for linha in cursor.fetchall(): 
        return(f"ID {linha[0]}| Título: {linha[1]} | Ano: {linha[2]} | Autor: {linha[3]} | Disponivel : {linha[4]}")
def update_dispon():
    conexao = sqlite3.connect("Biblioteca.db")
    cursor = conexao.cursor()

    cursor.execute("SELECT")
