# Importação da biblioteca sqlite3
import sqlite3

# Criar o banco de dados
produto = 'produtos.db'

# Criar tabelas
script_produtos = '''CREATE TABLE IF NOT EXISTS Produtos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco REAL NOT NULL,
    categoria TEXT NOT NULL,
    estoque INTEGER NOT NULL
);'''

try:
    with sqlite3.connect(produto) as con:
        # Criar um cursor
        cur = con.cursor()

        # Executar o script
        cur.execute(script_produtos)

        # Salvar as alterações no banco de dados
        con.commit()
        print('Tabela Criada com sucesso!')
except sqlite3.OperationalError as e:
    print('Erro:', e)

    # Verificar se a tabela foi criada
res = cur.execute('SELECT name FROM sqlite_master')
print(res.fetchall())  # retorna uma linha do resultado obtido, tabela
# resultado vem no formato de tupla
