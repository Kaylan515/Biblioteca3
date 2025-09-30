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

def update_dispon(id_livro):
    conexao = sqlite3.connect("Biblioteca.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT disponivel FROM Biblioteca WHERE id = ?", (id_livro,))
    resultado = cursor.fetchone()

    if resultado:
        status_atual = resultado[0]
        novo_status = "Não" if status_atual == "Sim" else "Sim"

        cursor.execute("""
            UPDATE Biblioteca
            SET disponivel = ?
            WHERE id = ?
        """, (novo_status, id_livro))
        conexao.commit()
        print(f"Disponibilidade do livro ID {id_livro} alterada para: {novo_status}")
    else:
        print(f"Erro: Livro com ID {id_livro} não encontrado.")
    conexao.close()

def remover_livro(id_livros):
    conexao = sqlite3.connect("Biblioteca.db")
    cursor = conexao.cursor()

    cursor.execute("DELETE FROM Biblioteca WHERE id = ?", (id_livros))
    linhas_afetadas = cursor.rowcount

    conexao.commit()
    conexao.close()

    if linhas_afetadas > 0:
        print(f"Livro com id {id_livros} removido com sucesso.")
    else:
        print(f"Erro: Livro com id {id_livros} não encontrado.")
