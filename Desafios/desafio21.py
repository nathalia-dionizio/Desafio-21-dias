"""
Desafio Construtor de Consultas SQL

Desafio
Neste desafio, você vai desenvolver um construtor de consultas SQL, um programa em Python que permite aos usuários criar consultas SQL SELECT personalizadas, comandos SQL UPDATE e comandos SQL INSERT. O construtor oferece uma interface interativa para coletar informações e gerar consultas ou comandos SQL com base nas escolhas dos usuários.

Funcionalidades do Construtor de Consultas SQL:
Consulta SQL SELECT
Os usuários podem criar consultas SQL SELECT personalizadas para recuperar dados de uma ou mais tabelas do banco de dados.
Eles podem selecionar as colunas desejadas, especificar tabelas e adicionar condições à cláusula WHERE, se necessário.
O programa gera e exibe a consulta SQL SELECT resultante.
Comando SQL UPDATE
Os usuários podem criar comandos SQL UPDATE para atualizar registros em uma tabela.
Eles devem fornecer o nome da tabela, as colunas e os novos valores que desejam atualizar.
Também podem adicionar condições à cláusula WHERE para especificar quais registros devem ser atualizados.
O programa gera e exibe o comando SQL UPDATE resultante.
Comando SQL INSERT
Os usuários podem criar comandos SQL INSERT para inserir novos registros em uma tabela.
Eles devem fornecer o nome da tabela, as colunas nas quais desejam inserir valores e os próprios valores.
O programa gera e exibe o comando SQL INSERT resultante.
Menu Interativo:
O programa apresenta um menu interativo que permite aos usuários escolher entre criar uma consulta SELECT, um comando UPDATE ou um comando INSERT.
Quais conhecimentos eu preciso adquirir para resolver este desafio?
Manipulação de strings em Python para construir os comandos SQL com base nas seleções dos usuários.
Interatividade com o usuário para coletar informações sobre colunas, tabelas, condições e valores desejados.
Conhecimento básico de SQL para entender as diferentes partes de um comando SQL (SELECT, UPDATE, INSERT, FROM, WHERE, SET, VALUES, etc.).
Testes
Após criar o seu código, abra o terminal, vá até a pasta que está seu script, e execute o comando abaixo.

python nome-do-seu-script.py
Você pode então realizar alguns testes em seu script. Execute seu script usando os valores abaixo, para ver se ele se comporta como esperado.

TESTE 01: Consulta SQL SELECT
- Usuário escolhe criar uma consulta SQL SELECT.
- Seleciona as colunas 'nome' e 'idade'.
- Seleciona a tabela 'usuarios'.
- Define uma condição WHERE 'idade > 25'.
- O programa gera e exibe a consulta SQL SELECT resultante.
- Resultado Esperado: 
  Consulta SQL gerada: "SELECT nome, idade FROM usuarios WHERE idade > 25".

TESTE 02: Comando SQL UPDATE
- Usuário escolhe criar um comando SQL UPDATE.
- Seleciona a tabela 'produtos'.
- Define as colunas e seus novos valores, por exemplo, 'preco = 29.99'.
- Define uma condição WHERE 'categoria = 'Eletrônicos''.
- O programa gera e exibe o comando SQL UPDATE resultante.
- Resultado Esperado: 
  Comando SQL gerado: "UPDATE produtos SET preco = 29.99 WHERE categoria = 'Eletrônicos'".

TESTE 03: Comando SQL INSERT
- Usuário escolhe criar um comando SQL INSERT.
- Seleciona a tabela 'clientes'.
- Especifica as colunas 'nome', 'email' e 'telefone'.
- Fornece os valores correspondentes, por exemplo, 'João Silva', 'joao@email.com', '(11) 1234-5678'.
- O programa gera e exibe o comando SQL INSERT resultante.
- Resultado Esperado: 
  Comando SQL gerado: "INSERT INTO clientes (nome, email, telefone) VALUES ('João Silva', 'joao@email.com', '(11) 1234-5678')".

TESTE 04: Consulta SQL SELECT
- Usuário escolhe criar uma consulta SQL SELECT.
- Seleciona as colunas 'titulo' e 'autor'.
- Seleciona a tabela 'livros'.
- Não define condições WHERE.
- O programa gera e exibe a consulta SQL SELECT resultante.
- Resultado Esperado: 
  Consulta SQL gerada: "SELECT titulo, autor FROM livros".

TESTE 05: Comando SQL INSERT
- Usuário escolhe criar um comando SQL INSERT.
- Seleciona a tabela 'funcionários'.
- Especifica as colunas 'nome', 'cargo' e 'salário'.
- Fornece os valores correspondentes, por exemplo, 'Maria', 'Gerente', 5500.
- O programa gera e exibe o comando SQL INSERT resultante.
- Resultado Esperado: 
  Comando SQL gerado: "INSERT INTO funcionários (nome, cargo, salário) VALUES ('Maria', 'Gerente', 5500)".

TESTE 06: Consulta SQL SELECT com Múltiplas Tabelas e Condições AND
- Usuário escolhe criar uma consulta SQL SELECT.
- Seleciona as colunas 'nome_cliente' e 'produto'.
- Seleciona as tabelas 'clientes' e 'compras'.
- Define as condições WHERE 'clientes.id = compras.cliente_id AND compras.data_compra >= '2022-01-01''.
- O programa gera e exibe a consulta SQL SELECT resultante.
- Resultado Esperado: 
  Consulta SQL gerada: "SELECT nome_cliente, produto FROM clientes, compras WHERE clientes.id = compras.cliente_id AND compras.data_compra >= '2022-01-01'".

Você pode fazer outros testes caso ache necessário.
"""
#resolução:

# Função para solicitar a seleção de colunas
def selecionar_colunas():
    colunas = input("\nDigite as colunas desejadas separadas por vírgula: ")
    return colunas

# Função para solicitar a seleção de tabelas
def selecionar_tabelas():
    tabelas = input("\nDigite as tabelas desejadas separadas por vírgula: ")
    return tabelas

# Função para solicitar as condições da cláusula WHERE
def selecionar_condicoes():
    condicoes = input("\nDigite as condições da cláusula WHERE: ")
    return condicoes

# Função para criar consultas SQL SELECT
def criar_consulta_select():
    colunas = selecionar_colunas()
    tabelas = selecionar_tabelas()
    condicoes = selecionar_condicoes()

    consulta_sql = f"SELECT {colunas} FROM {tabelas}"
    if condicoes:
        consulta_sql += f" WHERE {condicoes}"

    print("\nConsulta SQL SELECT gerada:")
    print(consulta_sql)

# Função para criar comandos SQL UPDATE
def criar_comando_update():
    tabela = input("\nDigite o nome da tabela que deseja atualizar: ")
    colunas_valores = input("\nDigite as colunas e valores a serem atualizados no formato 'coluna1 = valor1, coluna2 = valor2': ")
    condicoes = selecionar_condicoes()

    comando_sql = f"UPDATE {tabela} SET {colunas_valores}"
    if condicoes:
        comando_sql += f" WHERE {condicoes}"

    print("\nComando SQL UPDATE gerado:")
    print(comando_sql)

# Função para criar comandos SQL INSERT
def criar_comando_insert():
    tabela = input("\nDigite o nome da tabela em que deseja inserir os valores: ")
    colunas = input("Digite as colunas em que deseja inserir os valores, separadas por vírgula: ")
    valores = input("Digite os valores que deseja inserir, separados por vírgula: ")

    comando_sql = f"INSERT INTO {tabela} ({colunas}) VALUES ({valores})"

    print("\nComando SQL INSERT gerado:")
    print(comando_sql)

# Função principal
def main():
    while True:
        print("\nEscolha uma opção:")
        print("1. Criar Consulta SQL SELECT")
        print("2. Criar Comando SQL UPDATE")
        print("3. Criar Comando SQL INSERT")
        print("4. Sair")
        opcao = input("\nOpção: ")

        if opcao == "1":
            criar_consulta_select()
        elif opcao == "2":
            criar_comando_update()
        elif opcao == "3":
            criar_comando_insert()
        elif opcao == "4":
            print("\nSaindo do Construtor de Consultas SQL.\n")
            break
        else:
            print("\nOpção inválida. Tente novamente.\n")

if __name__ == "__main__":
    main()