"""
Desafio Jogo da Adivinhação

Desenvolva um jogo de adivinhação em que o usuário deve adivinhar um número gerado aleatoriamente pelo programa. O jogo deve ter as seguintes características:

O programa gera um número aleatório entre 1 e 100.
O jogador tem um número limitado de tentativas (7) para adivinhar o número correto.
Após cada tentativa, o programa fornece dicas sobre se o número correto é maior ou menor do que a tentativa atual do jogador.
O jogo continua até que o jogador adivinhe corretamente o número ou esgote todas as tentativas.
Quais conhecimentos eu preciso adquirir para resolver este desafio?
Geração de Números Aleatórios: Use o módulo random para gerar números aleatórios.
Input do jogador e Loops: Crie um loop para permitir que o jogador faça várias tentativas.
Condicionais: Use estruturas condicionais para fornecer dicas ao jogador com base em suas tentativas.
Dica importante
Sempre forneça feedback ao jogador após cada tentativa, dizendo se o número correto é maior, menor ou igual à sua tentativa atual.
A cada tentativa, além do feedback ele mostra quantas tentativas o jogador ainda tem.
Ao final do jogo, informe quantas tentativas o jogador levou para adivinhar o número correto e se ele venceu ou perdeu.
A cada acerto ele ganha um ponto
Crie um menu inicial que contém opções pra Jogar, Ver Pontuação, Zerar Pontuação, Sair
Testes
Após criar o seu código, abra o terminal, vá até a pasta que está seu script, e execute o comando abaixo.

python nome-do-seu-script.py
Você pode então realizar alguns testes em seu script. Execute seu script usando os valores abaixo, para ver se ele se comporta como esperado.

TESTE 01: O programa gera o número 42. O jogador chuta 50. O programa fornece a dica "O número é menor." O jogador chuta 30. O programa fornece a dica "O número é maior." O jogador chuta 40. O programa fornece a dica "O número é maior." O jogador chuta 41. O programa fornece a dica "O número é maior." O jogador chuta 42. O programa informa que o jogador acertou, ele ganha 1 ponto e mostra quantos pontos ele tem.
TESTE 02: O programa gera o número 67. O jogador faz 7 tentativas sem sucesso. O programa informa que o jogador perdeu, mas o jogo não é encerrado..
TESTE 03: O jogador pede pra ver sua pontuação.
TESTE 04: O jogador pede pra zerar sua pontuação.
TESTE 05: O jogador pede pra sair do jogo.
"""
#resolução:

def mostrar_menu():
# Exibe o menu de opções.
 print("#######################################")
 print("Jogo da adivinhação")
 print("#######################################")

import random

def adivinhar_numero():
    # Gera o número
    numero_gerado = random.randint(1, 100)
    print(f"O número X foi gerado com sucesso!")
    
    tentativas = 0 # Conta o número de tentativas do usuário
    acertou = False # Indica se o usuário acertou o número

    while not acertou and tentativas < 8:
        # Guarda o número que o usuário input
        resposta = input("Qual número de 1 a 100 você acha que é ? ")

        if resposta == str(numero_gerado):
            print(f"ACERTOU !!!")
            acertou = True # Encerra o loop
        else:
            tentativas += 1 # Incrementa o número de tentativas
            print(f"Ops ERROU! você tem mais {tentativas} tentativas")

        if tentativas == 8: # Se o usuário fez 8 tentativas, ele perde o jogo
            print(f"Ops você perdeu o jogo, que tal jogar de novo ? O número era {numero_gerado}.")
            break # Sai do loop


mostrar_menu()
adivinhar_numero()