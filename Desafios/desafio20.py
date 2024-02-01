# Importando a biblioteca random para embaralhar as perguntas
import random
"""
Desafio Quiz de Conhecimentos Gerais
Desenvolva um pequeno quiz de múltipla escolha com perguntas e respostas. O programa deve mostrar uma pergunta com opções de resposta e permitir que o usuário escolha uma. No final, o programa deve mostrar a pontuação do usuário.

Quais conhecimentos eu preciso adquirir para resolver este desafio?
Estruturas de controle para lógica de perguntas e respostas: Aprenda a criar a lógica do quiz.
Manipulação de listas e dicionários: Use para armazenar as perguntas, opções de resposta e verificar as respostas corretas.
Funções de entrada e saída: Entenda como interagir com o usuário para obter respostas e mostrar perguntas e pontuações.
Dica importante
Crie uma estrutura de dados para armazenar as perguntas, opções de resposta e a resposta correta.
Implemente um loop para apresentar as perguntas ao usuário e permitir que ele escolha uma resposta.
Mantenha a contagem de respostas corretas e, no final do quiz, mostre a pontuação do usuário.
Você pode criar diferentes níveis de dificuldade ou categorias de perguntas para tornar o quiz mais interessante.
Testes
Após criar o seu código, abra o terminal, vá até a pasta que está seu script, e execute o comando abaixo.

python nome-do-seu-script.py
Você pode então realizar alguns testes em seu script. Execute seu script usando os valores abaixo, para ver se ele se comporta como esperado.

TESTE 01: Teste com perguntas e respostas corretas

Pergunta 1: Qual é a capital do Brasil?
Resposta correta: Brasília
Pergunta 2: Quem escreveu "Dom Quixote"?
Resposta correta: Miguel de Cervantes
Pergunta 3: Qual é o maior planeta do sistema solar?
Resposta correta: Júpiter
Resposta do usuário: Brasília, Miguel de Cervantes, Júpiter
Resultado esperado: O programa deve mostrar a pontuação do usuário (3/3).

TESTE 02: Teste com perguntas e respostas incorretas

Pergunta 1: Qual é a capital da Argentina?
Resposta correta: Buenos Aires
Pergunta 2: Qual é o maior rio do mundo?
Resposta correta: Rio Amazonas
Pergunta 3: Quem pintou a "Mona Lisa"?
Resposta correta: Leonardo da Vinci
Resposta do usuário: Rio de Janeiro, Rio Nilo, Van Gogh
Resultado esperado: O programa deve mostrar a pontuação do usuário (0/3) e indicar quais respostas estavam corretas.

TESTE 03: Teste com mistura de respostas corretas e incorretas

Pergunta 1: Quem é o autor de "Romeu e Julieta"?
Resposta correta: William Shakespeare
Pergunta 2: Qual é o símbolo químico do oxigênio?
Resposta correta: O
Pergunta 3: Qual é a capital da Alemanha?
Resposta correta: Berlim
Resposta do usuário: William Shakespeare, O, Paris
Resultado esperado: O programa deve mostrar a pontuação do usuário (2/3) e indicar quais respostas estavam corretas.

Você pode fazer outros testes caso ache necessário.

"""
#resolução:

# Definindo as perguntas e respostas
questions = {
    "Qual é a capital do Brasil?": ["São Paulo", "Rio de Janeiro", "Brasília", "Belo Horizonte"],
    "Qual é o maior planeta do sistema solar?": ["Júpiter", "Saturno", "Urano", "Netuno"],
    "Qual é o maior animal terrestre?": ["Elefante", "Rinoceronte", "Girafa", "Hipopótamo"],
    "Qual é o maior oceano do mundo?": ["Oceano Atlântico", "Oceano Índico", "Oceano Pacífico", "Oceano Ártico"]
}

# Embaralhando as perguntas
questions_list = list(questions.items())
random.shuffle(questions_list)

# Inicializando a pontuação do usuário
score = 0

# Iterando sobre as perguntas
for question, choices in questions_list:
    # Embaralhando as opções de resposta
    random.shuffle(choices)

    # Exibindo a pergunta e as opções de resposta
    print(question)
    for i, choice in enumerate(choices):
        print(f"{i + 1}. {choice}")

    # Obtendo a resposta do usuário
    answer = int(input("Escolha uma opção: "))

    # Verificando se a resposta está correta
    if choices[answer - 1] == questions[question][0]:
        print("Resposta correta!")
        score += 1
    else:
        print(f"Resposta incorreta. A resposta correta é {questions[question][0]}.")

# Exibindo a pontuação final do usuário
print(f"Sua pontuação final é {score} de {len(questions)}.")
