import random
"""
Desafio Jogo do Número Primo

Desenvolva um jogo que gera aleatoriamente um número e o jogador deve determinar se esse número é primo ou não. O jogador ganha pontos por cada resposta correta.

Quais conhecimentos eu preciso adquirir para resolver este desafio?
Lógica para verificar números primos: Aprenda a lógica matemática por trás dos números primos.
Geração de Números Aleatórios: Use o módulo random para gerar números aleatórios.
Criação de funções para organizar melhor o seu código.
Input do jogador e Condições: Receba a resposta do jogador e verifique se está correta.
Dica importante
Um número primo é aquele que só é divisível por 1 e por ele mesmo. Você pode criar uma função que verifica se um número é primo ou não, e então usá-la para determinar a resposta do jogador.
A cada acerto ele ganha um ponto
Crie um menu inicial que contém opções pra Jogar, Ver Pontuação, Zerar Pontuação, Sair
Testes
Após criar o seu código, abra o terminal, vá até a pasta que está seu script, e execute o comando abaixo.

python nome-do-seu-script.py
Você pode então realizar alguns testes em seu script. Execute seu script usando os valores abaixo, para ver se ele se comporta como esperado.

TESTE 01: O programa gera o número 7. O jogador responde "Primo". A resposta está correta, e o jogador ganha pontos.
TESTE 02: O programa gera o número 10. O jogador responde "Não Primo". A resposta está correta, e o jogador ganha pontos.
TESTE 03: O programa gera o número 15. O jogador responde "Primo". A resposta está incorreta, e o jogador não ganha pontos e o jogo acaba.
TESTE 04: O programa gera o número 3. O jogador responde "Não Primo". A resposta está incorreta, e o jogador não ganha pontos e o jogo acaba.
TESTE 05: O jogador escolhe a opção de ver sua pontuação e ela está correta.
TESTE 06: O jogador escolhe a opção de zerar sua pontuação e ao jogar novamente e acertar, sua pontuação vai pra 1.
TESTE 07: O jogador escolhe a opção de sair.

"""
#resolução:

import random

def mostrar_menu():
# Exibe o menu de opções.
 print("#######################################")
 print("Jogo do Número Primo")
 print("#######################################")

def is_prime(n):
    """
    Retorna True se n é primo, False caso contrário.
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def play_game():
    pontuacao = 0
    while True:
        # Gera um número aleatório entre 1 e 100.
        number = random.randint(1, 100)
        # Pergunta ao jogador se o número é primo.
        answer = input(f"O número {number} é primo? (s/n) ")
        # Verifica se a resposta do jogador está correta.
        if (answer == "s" and is_prime(number)) or (answer == "n" and not is_prime(number)):
            print("Correto!")
            pontuacao += 1
        else:
            print("Incorreto!")
            break
    print(f"Sua pontuação é {pontuacao}.")

# Joga o jogo.
mostrar_menu()    
play_game()


    
    