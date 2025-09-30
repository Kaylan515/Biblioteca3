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

    if livros_data:    
        headers = ["ID", "Título", "Autor", "Ano", "Disponível"]
        
        tabela_completa = [headers] + list(livros_data)
        
        st.table(tabela_completa)
        
    else:
        st.info("Nenhum livro cadastrado. Use a aba 'Cadastrar Novo Livro'.")

elif opcao == "Cadastrar Novo Livro":
    st.header("Cadastrar Novo Livro")
    
    with st.form("form_cadastro"):
        titulo = st.text_input("Título", max_chars=100)
        autor = st.text_input("Autor", max_chars=100)
        ano = st.number_input("Ano", min_value=1000, max_value=2100, step=1, value=2023)
        
        submitted = st.form_submit_button("Cadastrar Livro")

        if submitted:
            if titulo and autor:
                funcoes.cadastrar_livro(titulo, autor, ano) 
                st.success(f"Livro '{titulo}' cadastrado com sucesso!")
            else:
                st.error("Título e Autor são obrigatórios.")

elif opcao == "Atualizar/Remover Livro":
    st.header("Gerenciamento de Livros")
    
    
    st.warning("Para Atualizar ou Remover, digite o ID e clique em apenas um botão.")
    
    id_selecionado = st.number_input("Digite o ID do livro", min_value=1, step=1, key="manage_id")

    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🔄 Alterar Disponibilidade"):
            if id_selecionado:
                funcoes.update_dispon(id_selecionado) 
                st.success(f"Disponibilidade do ID {id_selecionado} alterada.")
                st.experimental_rerun()
            else:
                st.warning("Insira um ID.")

    with col2:
        if st.button("🗑️ Remover Livro"):
            if id_selecionado:
                funcoes.remover_livro(id_selecionado) 
                st.success(f"Livro ID {id_selecionado} removido.")
                st.experimental_rerun()
            else:
                st.warning("Insira um ID.")

    st.markdown("---")
    st.subheader("Livros Atuais (para referência de ID):")
    funcoes.listar_livro()
