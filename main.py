import funcoes
import sqlite3
def cadastrar_livro(título, autor, ano):
    conn = sqlite3.connect("Biblioteca.db")
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO Biblioteca (título, autor, ano)
    VALUES (?, ?, ?, ?)
    """, (título, autor, ano, "Sim"))
título = input("Insira o título do livro que quer cadastrar: ")
autor = input("Nome do autor: ")
ano = int(input("Ano de lançamento: "))
funcoes.cadastrar_livro(título,autor,ano)