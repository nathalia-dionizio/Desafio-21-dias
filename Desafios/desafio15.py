import csv

"""
Desafio Gerenciador de Biblioteca Pessoal

Desenvolva um programa em Python que permita ao usuário inserir informações sobre livros em sua biblioteca pessoal e, em seguida, visualizar a lista de livros disponíveis.

Quais conhecimentos eu preciso adquirir para resolver este desafio?
Leitura e Escrita de Arquivos CSV: Aprenda a ler e escrever dados em um arquivo CSV.
Manipulação de Listas: Pratique como adicionar, remover e listar itens em uma lista.
Estruturas de Controle: Utilize estruturas de controle, como loops e condicionais, para criar um menu interativo para o usuário.
Dica importante
Certifique-se de criar um arquivo CSV vazio para armazenar os detalhes dos livros, com as colunas apropriadas para título do livro, autor e ano de publicação.
Implemente um menu de opções para o usuário, permitindo que ele insira novos livros ou visualize a lista de livros existentes.
Utilize loops e estruturas condicionais para criar um programa interativo.
Ao ler os dados do arquivo CSV, certifique-se de apresentar os livros de forma legível para o usuário, por exemplo, em um formato de lista.
A utilização de arquivos CSV visa guardar os dados entre as execuções, então, caso adicione livro e saia do programa, ao entrar novamente e listar os livros cadastrados, eles estarão lá.
Testes
Após criar o seu código, abra o terminal, vá até a pasta que está seu script, e execute o comando abaixo.

python nome-do-seu-script.py
Você pode então realizar alguns testes em seu script. Execute seu script usando os valores abaixo, para ver se ele se comporta como esperado.

TESTE 01: Adicionar um novo livro à biblioteca e verificá-lo na lista.
TESTE 02: Adicionar vários livros à biblioteca e verificar se todos estão na lista.
TESTE 03: Visualizar a lista de livros na biblioteca vazia.
TESTE 04: Inserir livros na biblioteca e depois fechar o programa. Ao reiniciar o programa, verificar se os livros ainda estão na lista.

"""
#resolução:

import csv

def adicionar_livro():
    titulo = input('Digite o título do livro: ')
    autor = input('Digite o nome do autor: ')
    ano = input('Digite o ano de publicação: ')

    with open('biblioteca.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([titulo, autor, ano])

    print('Livro adicionado com sucesso!')

def listar_livros():
    with open('biblioteca.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

while True:
    print('Selecione uma opção:')
    print('1. Adicionar livro')
    print('2. Listar livros')
    print('3. Sair')

    opcao = input()

    if opcao == '1':
        adicionar_livro()
    elif opcao == '2':
        listar_livros()
    elif opcao == '3':
        break
    else:
        print('Opção inválida. Tente novamente.')


