"""
Desafio Jogo da Forca

Desafio
Desenvolva uma versão simples do jogo da forca, onde o usuário tenta adivinhar uma palavra escolhida aleatoriamente pelo programa.

Quais conhecimentos eu preciso adquirir para resolver este desafio?
Manipulação de Strings e Loops: Aprenda a manipular strings e criar loops para o processo de adivinhação.
Escolha Aleatória de Palavras: Use o módulo random para selecionar palavras de uma lista.
Dica importante
Comece com uma lista de palavras que serão escolhidas aleatoriamente pelo programa.
Implemente um sistema que oculte a palavra e revele letras à medida que o usuário adivinha.
Defina um número de tentativas para o usuário e atualize-o à medida que eles fazem tentativas incorretas.
Crie um controle quando o usuário chutar uma letra que ele já chutou antes
Testes
Após criar o seu código, abra o terminal, vá até a pasta que está seu script, e execute o comando abaixo.

python nome-do-seu-script.py
Você pode então realizar alguns testes em seu script.

"""
#resolução:

import random

def palavra():
    palavras = ['abacaxi', 'banana', 'caju', 'damasco', 'figo', 'goiaba', 'laranja', 'manga', 'nectarina', 'pera']
    return random.choice(palavras)

def jogo_da_forca():
    palavra_secreta = palavra()
    senha_list = [l for l in palavra_secreta]
    chances = 6
    tentativas = []
    while chances > 0:
        erros = 0
        for i in senha_list:
            if i in tentativas:
                print(i, end=' ')
            else:
                print('_', end=' ')
                erros += 1
        if erros == 0:
            print('\nParabéns! Você ganhou!')
            break
        tentativa = input('\nDigite uma letra: ').lower()
        tentativas.append(tentativa)
        if tentativa not in senha_list:
            chances -= 1
            print('\nLetra errada. Você tem mais', chances, 'tentativas.')
            if chances == 0:
                print('\nVocê perdeu. A palavra era', palavra_secreta)
        else:
            print('\nLetra correta!')
    jogar_novamente = input('Deseja jogar novamente? (s/n) ')
    if jogar_novamente == 's':
        jogo_da_forca()
    else:
        print('Obrigado por jogar!')
        
jogo_da_forca()
