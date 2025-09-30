import streamlit as st
import funcoes
import sqlite3

funcoes.inicializar_banco() 

st.set_page_config(layout="wide")
st.title("📚 Sistema de Gerenciamento de Biblioteca")

st.sidebar.title("Menu")
opcao = st.sidebar.selectbox("Escolha uma Operação", 
                            ("Listar Livros", "Cadastrar Novo Livro", 
                             "Atualizar/Remover Livro"))

if opcao == "Listar Livros":
    st.header("Catálogo Completo")
    
    conexao = sqlite3.connect("Biblioteca.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT id, título, autor, ano, disponivel FROM Biblioteca")
    livros_data = cursor.fetchall()
    conexao.close()
