"""
Desafio Lista de Tarefas

Desenvolva uma aplicação simples para gerenciar uma lista de tarefas, permitindo adicionar e remover itens.

Dica importante
Você pode usar uma lista em Python para armazenar as tarefas. Crie funções que permitam adicionar tarefas à lista, remover tarefas existentes e listar todas as tarefas.
Ofereça um menu ao usuário com opções para adicionar uma nova tarefa, remover uma tarefa existente, listar todas as tarefas e sair.
Lembre que você não pode encerrar seu programa ao realizar uma ação, ele tem sempre que ficar ativo pois ao ser encerrado, todos os dados inseridos anteriormente são perdidos, portanto, você pode contruir seu código num loop infinito (while True) até que o usuário escolha a opção de sair.
Considere tratar casos em que o usuário tenta remover uma tarefa que não existe na lista.
Testes
Após criar o seu código, abra o terminal, vá até a pasta que está seu script, e execute o comando abaixo.

python nome-do-seu-script.py
Você pode então realizar alguns testes em seu script. Execute seu script usando os valores abaixo, para ver se ele se comporta como esperado.

TESTE 01: Adicione várias tarefas à lista e verifique se elas são exibidas corretamente.
TESTE 02: Remova tarefas da lista e certifique-se de que a remoção seja bem-sucedida.
TESTE 03: Liste todas as tarefas e verifique se elas estão sendo exibidas corretamente.
TESTE 04: Teste situações em que o usuário tenta remover uma tarefa que não existe na lista.
TESTE 05: Teste situações em que o usuário tenta remover uma tarefa mas a lista está vazia.
TESTE 06: Teste situações em que o usuário tenta mostrar todas as tarefas mas a lista está vazia.
Você pode fazer outros testes caso ache necessário.

"""
#resolução:

# Cria uma lista vazia para armazenar as tarefas
tarefas = []

# Define uma função para adicionar uma tarefa à lista
def adicionar_tarefa():
  # Pede ao usuário que digite a tarefa
  tarefa = input("Digite a tarefa que deseja adicionar: ")
  # Adiciona a tarefa à lista
  tarefas.append(tarefa)
  # Mostra uma mensagem de confirmação
  print(f"Tarefa '{tarefa}' adicionada com sucesso!")

# Define uma função para remover uma tarefa da lista
def remover_tarefa():
  # Pede ao usuário que digite o número da tarefa que deseja remover
  numero = int(input("Digite o número da tarefa que deseja remover: "))
  # Verifica se o número é válido
  if numero > 0 and numero <= len(tarefas):
    # Remove a tarefa da lista
    tarefa = tarefas.pop(numero - 1)
    # Mostra uma mensagem de confirmação
    print(f"Tarefa '{tarefa}' removida com sucesso!")
  else:
    # Mostra uma mensagem de erro
    print("Número inválido!")

# Define uma função para listar todas as tarefas da lista
def listar_tarefas():
  # Verifica se a lista está vazia
  if len(tarefas) == 0:
    # Mostra uma mensagem informando que não há tarefas
    print("Não há tarefas na lista.")
  else:
    # Mostra as tarefas da lista com seus respectivos números
    print("Tarefas da lista:")
    for i, tarefa in enumerate(tarefas):
      print(f"{i + 1} - {tarefa}")

# Define uma função para mostrar o menu de opções ao usuário
def mostrar_menu():
  # Mostra as opções disponíveis
  print("Escolha uma opção:")
  print("1 - Adicionar uma nova tarefa")
  print("2 - Remover uma tarefa existente")
  print("3 - Listar todas as tarefas")
  print("4 - Sair")
  # Pede ao usuário que digite a opção desejada
  opcao = int(input("Digite a opção: "))
  # Retorna a opção escolhida
  return opcao

# Cria um loop infinito para executar o programa
while True:
  # Mostra o menu ao usuário
  opcao = mostrar_menu()
  # Verifica qual opção foi escolhida
  if opcao == 1:
    # Chama a função para adicionar uma tarefa
    adicionar_tarefa()
  elif opcao == 2:
    # Chama a função para remover uma tarefa
    remover_tarefa()
  elif opcao == 3:
    # Chama a função para listar as tarefas
    listar_tarefas()
  elif opcao == 4:
    # Encerra o programa
    print("Obrigado por usar o programa. Até mais!")
    break
  else:
    # Mostra uma mensagem de erro
    print("Opção inválida!")
