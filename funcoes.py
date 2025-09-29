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

