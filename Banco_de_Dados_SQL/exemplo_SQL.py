# SQL -> Structure Query Language
# db.sqlite3
import sqlite3

with sqlite3.connect('artistas.db') as conexao:
    # Criar conexao com o banco de dados
    sql = conexao.cursor()
    # Rodar comando SQL
    #sql.execute('create table banda(nome text, estilo text, membros interger);')
    # Exemplo de inserir dados
    #sql.execute('insert into banda(nome, estilo, membros) values ("UB40", "Reggae", 6)')
    # Exemplo de usar dados da minha aplicacao em um comando SQL
    nome = input('Digite o nome da banda: ')
    estilo = input('Digite o estilo da banda: ')
    quantidade_integrantes = int(input('Digite a quantidade de integrantes da banda: '))
    
    sql.execute('insert into banda values(?,?,?)', [nome, estilo, quantidade_integrantes])
    # Salvando alteracoes no Banco de Dados
    conexao.commit()
    
    # Exibir dados no console Python (Terminal)
    bandas = sql.execute('select * from banda;')
    for banda in bandas:
        print(banda)
        