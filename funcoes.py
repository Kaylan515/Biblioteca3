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
    try:
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
    except Exception as error:
        print(f"Um {error} foi encontrado")
        print(f"Disponibilidade do livro ID {id_livro} alterada para: {novo_status}")
    else:
        print(f"Erro: Livro com ID {id_livro} não encontrado.")
        conexao.close()

def remover_livro(id_livros):
    try:
        conexao = sqlite3.connect("Biblioteca.db")
        cursor = conexao.cursor()

        cursor.execute("DELETE FROM Biblioteca WHERE id = ?", (id_livros,))
        linhas_afetadas = cursor.rowcount

        conexao.commit()
    except Exception as error:
        print(f"Um {error} foi encontrado")
    finally:
        print("fechamento sendo iniciado")
        conexao.close()

        if linhas_afetadas > 0:
            print(f"Livro com id {id_livros} removido com sucesso.")
        else:
            print(f"Erro: Livro com id {id_livros} não encontrado.")

def menu_interativo():
    while True:
        print("\n==============================")
        print("    Menu da Biblioteca")
        print("==============================")
        print("1. Cadastrar livro")
        print("2. Listar livros")
        print("3. Atualizar disponibilidade")
        print("4. Remover livro")
        print("5. Sair")
        print("_________________________________")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            print("--- CADASTRO DE LIVRO ---")
            titulo = input("Título: ")
            autor = input("Autor: ")
            while True:
                    try:
                        ano = int(input("Ano: "))
                        break
                    except ValueError:
                        print("Por favor, digite um ano válido (número inteiro).")
            cadastrar_livro(titulo, autor, ano)

        elif escolha == '2':
                listar_livro()

        elif escolha == '3':
                if listar_livro():
                    try:
                        id_livro = int(input("\nDigite o ID do livro para atualizar a disponibilidade: "))
                        update_dispon(id_livro)
                    except ValueError:
                        print("Por favor, digite um ID válido (número inteiro).")

        elif escolha == '4':
                if listar_livro():
                    try:
                        id_livro = int(input("\nDigite o ID do livro para REMOVER: "))
                        remover_livro(id_livro)
                    except ValueError:
                        print("Por favor, digite um ID válido (número inteiro).")

        elif escolha == '5':
                print("Saindo da aplicação. Até mais!")
                break
        else:
                print("Opção inválida. Por favor, escolha uma opção de 1 a 5.")

