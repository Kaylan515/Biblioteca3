import funcoes
import sqlite3
conexao = sqlite3.connect("Biblioteca.db")
cursor = conexao.cursor()

cursor.execute("""
 CREATE TABLE IF NOT EXISTS Biblioteca(
         id INTEGER PRIMARY KEY AUTOINCREMENT,
         titulo TEXT NOT NULL,  
         autor TEXT NOT NULL,
        ano INTEGER,
         disponivel TEXT)
      """)

conexao.commit()
conexao.close()
titulo = input("Digite o titulo do livro que deseja cadastrar: ")
autor = input("Digite o autor do livro: ")
ano = int(input("Insirar o ano do livro: "))

funcoes.cadastrar_livro(titulo,autor,ano)

# print(funcoes.listar_livro())
# id_disponivel = int(input("Digite o id do livro alterado ou removido: "))
# funcoes.update_dispon(id_disponivel)
# funcoes.remover_livro(id_disponivel)


