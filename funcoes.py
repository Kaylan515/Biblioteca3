import sqlite3
def criar_pasta():
    conn = sqlite3.connect("Biblioteca.db")
    cursor = conn.cursor()
    cursor.execute("""
  CREATE TABLE IF NOT EXISTS biblioteca (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      título TEXT NOT NULL,
      autor TEXT NOT NULL,
      ano INTERGER,
      disponivel TEXT   
      )
 """)
    conn.commit()
    conn.close()

def cadastrar_livro(título, autor, ano):
    conn = sqlite3.connect("Biblioteca.db")
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO Biblioteca (título, autor, ano)
    VALUES (?, ?, ?, ?)
    """, (título, autor, ano, "Sim")
    )

    conn.commit()
    conn.close()