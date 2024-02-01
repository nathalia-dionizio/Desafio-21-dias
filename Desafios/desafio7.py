import time

"""
Desafio Temporizador/Contador

Crie um programa que funcione como um temporizador (contagem progressiva) ou contador regressivo. O usuário vai poder escolher entre as duas opções.

Quais conhecimentos eu preciso adquirir para resolver este desafio?
Módulo time: Aprenda a usar o módulo time para criar um temporizador.
Loops e Condições: Use loops e condições para controlar o tempo.
Dica importante
Você pode usar o módulo time para realizar contagens regressivas. Inicie um temporizador com um determinado tempo (em segundos) e crie um loop que decremente esse tempo a cada segundo até que atinja zero.
Você pode oferecer opções ao usuário, como definir o tempo desejado para o temporizador ou escolher entre um temporizador regressivo e um contador progressivo.
Mostre o tempo restante de forma clara para o usuário enquanto o temporizador estiver em andamento.
Testes
Após criar o seu código, abra o terminal, vá até a pasta que está seu script, e execute o comando abaixo.

python nome-do-seu-script.py
Você pode então realizar alguns testes em seu script. Execute seu script usando os valores abaixo, para ver se ele se comporta como esperado.

TESTE 01: Crie um temporizador de 12 segundos e verifique se ele funciona corretamente.
TESTE 02: Crie um contador regressivo de 12 segundos e verifique se ele funciona corretamente.
"""
#resolução:

# menu de opções
def mostrar_menu():
  print("Escolha uma opção:")
  print("1 - Temporizador regressivo")
  print("2 - Contador progressivo")
  print("3 - Sair")

# temporizador regressivo
def temporizador_regressivo():
  # Pede ao usuário o tempo desejado em segundos
  tempo = int(input("Digite o tempo em segundos: "))
  # Enquanto o tempo não for zero, mostra o tempo restante e diminui um segundo
  while tempo > 0:
    print(f"Tempo restante: {tempo} segundos")
    time.sleep(1)
    tempo -= 1
  # Mostra uma mensagem quando o tempo acabar
  print("Tempo esgotado!")

# Função para executar o contador progressivo
def contador_progressivo():
  # Inicializa o contador com zero
  contador = 0
  # Pede ao usuário o tempo desejado em segundos
  tempo = int(input("Digite o tempo em segundos: "))
  while contador < tempo: # Usa o contador como condição do loop
    print(f"Contador: {contador} segundos")
    time.sleep(1) # Pausa o programa por um segundo
    contador += 1 # Incrementa o contador
  # Mostra uma mensagem quando chegar no tempo desejado
  print(f"Oba deu o tempo de: {tempo} segundos")

# menu de opções
mostrar_menu()
# Pede ao usuário que escolha uma opção
opcao = int(input("Digite a opção desejada: "))
# Executa a opção escolhida
if opcao == 1:
  temporizador_regressivo()
elif opcao == 2:
  contador_progressivo()
elif opcao == 3:
  print("Programa encerrado")
else:
  print("Opção inválida")
