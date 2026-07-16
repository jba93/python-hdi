import sqlite3

# Conectar o banco de dados (ou criar um novo se ainda não existir)
def conectarBanco():
    conexao = sqlite3.connect("meu_banco.db")
    return conexao

# Criar uma tabela
def criarTabela():
    conexao = conectarBanco()
    cursor = conexao.cursor()
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                idade INTEGER
            )
    ''')
    conexao.commit() # Executa de fato o comando
    conexao.close() # Fecha a conexão

# Inserir informações na tabela
def inserirUsuario(nome, idade):
    conexao = conectarBanco()
    cursor = conexao.cursor() # Preciso do cursor para realizar execuções
    cursor.execute('''
            INSERT INTO usuarios(nome, idade)
            VALUES (?, ?)
    ''', (nome, idade))
    conexao.commit() # Executa de fato o comando
    conexao.close() # Fecha a conexão

def listarUsuarios():
    conexao = conectarBanco()
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM usuarios')
    usuarios = cursor.fetchall()
    # Aqui não precisa do commit, commit é apenas para alterações no Banco de Dados
    for usuario in usuarios:
        print(usuario)
    conexao.close()

def atualizarUsuario(id, novoNome, novaIdade):
    conexao = conectarBanco()
    cursor = conexao.cursor()
    cursor.execute('''
                UPDATE usuarios
                SET nome = ?, idade = ?
                WHERE id = ?
    ''', (novoNome, novaIdade, id)) # Se colocasse essas variáveis no lugar do ? precisaria de todo tratamento para strings
    conexao.commit()
    conexao.close()

def excluirUsuario(id):
    conexao = conectarBanco()
    cursor = conexao.cursor()
    cursor.execute('''
                DELETE FROM usuarios
                WHERE id = ?
    ''', (id,)) # Atenção para a VÍRGULA, pois geralmente é necessário usar mais de um argumento
    conexao.commit()
    conexao.close()

# Usando as funções
# Inserimos dados  na tabela:
inserirUsuario("Caio", 39)
inserirUsuario("Juliana", 33)
inserirUsuario("Lucas", 31)

# Exibir dados da tabela
print("Usuários antes de atualizar:")
listarUsuarios()

# Altera usuários da tabela
atualizarUsuario(3, "Luccas", 44)
atualizarUsuario(1, "Python", 45)

# Exibir dados da tabela
print("Usuários depois de atualizar:")
listarUsuarios()

# Exclui usuários da tabela
excluirUsuario(1)
excluirUsuario(2)
excluirUsuario(15)

# Exibir dados da tabela
print("Usuários depois de excluir:")
listarUsuarios()