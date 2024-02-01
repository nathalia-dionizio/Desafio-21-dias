"""
Desafio Agenda de Contatos

Crie um programa que funcione como uma agenda de contatos. Deve ser possível adicionar, listar, buscar e excluir contatos. Cada contato deve ter nome, número de telefone e e-mail.

Quais conhecimentos eu preciso adquirir para resolver este desafio?
Manipulação de listas e dicionários em Python: Aprenda a criar e manipular essas estruturas para armazenar dados dos contatos.
Estruturas de controle (if, else, loops): Use essas estruturas para implementar as funcionalidades da agenda.
Funções básicas de entrada e saída: Pratique a obtenção de dados do usuário e exibição de informações.
Dica importante
Utilize um dicionário para representar cada contato, onde as chaves do dicionário representam os campos (nome, número de telefone e e-mail).
Implemente um menu de opções para o usuário escolher entre adicionar, listar, buscar e excluir contatos.
Lide com erros ou situações excepcionais, como contatos duplicados ou buscas que não encontram nenhum contato.
Testes
Após criar o seu código, abra o terminal, vá até a pasta que está seu script, e execute o comando abaixo.

python nome-do-seu-script.py
Você pode então realizar alguns testes em seu script. Execute seu script usando os valores abaixo, para ver se ele se comporta como esperado.

TESTE 01: Teste de adição de contato

Nome: João Silva
Número de telefone: (11) 98765-4321
E-mail: joao@example.com
Resultado esperado: O programa deve adicionar o contato à agenda.

TESTE 02: Teste de adição de contato
Nome: Maria Santos
Número de telefone: (81) 91234-5678
E-mail: joao@example.com
Resultado esperado: O programa deve adicionar o contato à agenda.

TESTE 03: Teste de listagem de contatos
Resultado esperado: O programa deve listar todos os contatos da agenda.

TESTE 04: Teste de busca de contato existente
Nome a ser buscado: Maria Santos
Resultado esperado: O programa deve encontrar o contato de Maria Santos e exibir suas informações.

TESTE 05: Teste de busca de contato inexistente
Nome a ser buscado: Carlos Oliveira
Resultado esperado: O programa deve informar que o contato não foi encontrado.

TESTE 06: Teste de exclusão de contato existente:
Nome a ser excluído: João Silva
Resultado esperado: O programa deve remover o contato de João Silva da agenda.

TESTE 07: Teste de exclusão de contato inexistente:
Nome a ser excluído: Ana Silva
Resultado esperado: O programa deve informar que o contato não foi encontrado.
Você pode fazer outros testes caso ache necessário.

"""
#resolução:

contatos = []

def adicionar_contato():
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o número de telefone do contato: ")
    email = input("Digite o endereço de e-mail do contato: ")
    contato = {"nome": nome, "telefone": telefone, "email": email}
    if contato in contatos:
        print("Este contato já existe na agenda.")
    else:
        contatos.append(contato)
        print("Contato adicionado com sucesso.")

def listar_contatos():
    if not contatos:
        print("A agenda está vazia.")
    else:
        for i, contato in enumerate(contatos):
            print(f"{i + 1}. Nome: {contato['nome']}, Telefone: {contato['telefone']}, E-mail: {contato['email']}")

def buscar_contato():
    termo = input("Digite o nome do contato que deseja buscar: ")
    resultados = []
    for contato in contatos:
        if termo.lower() in contato["nome"].lower():
            resultados.append(contato)
    if not resultados:
        print("Nenhum contato encontrado.")
    else:
        for i, contato in enumerate(resultados):
            print(f"{i + 1}. Nome: {contato['nome']}, Telefone: {contato['telefone']}, E-mail: {contato['email']}")

def excluir_contato():
    termo = input("Digite o nome do contato que deseja excluir: ")
    removidos = 0
    for contato in contatos:
        if termo.lower() == contato["nome"].lower():
            contatos.remove(contato)
            removidos += 1
    if removidos == 0:
        print("Nenhum contato encontrado.")
    else:
        print(f"{removidos} contato(s) removido(s) com sucesso.")

while True:
    print("\nAgenda de Contatos")
    print("1. Adicionar Contato")
    print("2. Listar Contatos")
    print("3. Buscar Contato")
    print("4. Excluir Contato")
    print("5. Sair")
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        adicionar_contato()
    elif opcao == "2":
        listar_contatos()
    elif opcao == "3":
        buscar_contato()
    elif opcao == "4":
        excluir_contato()
    elif opcao == "5":
        break
    else:
        print("Opção inválida. Tente novamente.")
