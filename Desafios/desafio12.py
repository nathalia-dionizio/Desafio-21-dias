"""
Desafio Análise de Frequência de Letras

Desenvolva um programa que analise a frequência de cada letra em um texto fornecido pelo usuário.
Quais conhecimentos eu preciso adquirir para resolver este desafio?
Manipulação de Strings: Aprenda a contar a frequência de caracteres e a checar se um determinado caractere é uma letra (pode utilizar a função isalpha()).
Manipulação de Dicionários: Aprenda a adicionar, obter e atualizar dados em um dicionário.
Loops em Strings: Pratique a iteração em strings para análise.
Dica importante
Use um dicionário para rastrear a contagem de cada letra no texto.
Certifique-se de tratar letras maiúsculas e minúsculas da mesma forma para obter resultados precisos.
Ignore espaços em branco, pontuações, números e caracteres especiais no texto, se desejar contar apenas letras. Considere o uso da função isalpha() para verificar se um caractere é uma letra antes de contar.
Testes
Após criar o seu código, abra o terminal, vá até a pasta que está seu script, e execute o comando abaixo.

python nome-do-seu-script.py
Você pode então realizar alguns testes em seu script. Execute seu script usando os valores abaixo, para ver se ele se comporta como esperado.

TESTE 01:
Texto fornecido: "hello world"
Resultado esperado: 
{
    'h': 1,
    'e': 1,
    'l': 3,
    'o': 2,
    'w': 1,
    'r': 1,
    'd': 1
}

TESTE 02:
Texto fornecido: "programming is fun"
Resultado esperado:
{
    'p': 1,
    'r': 2,
    'o': 1,
    'g': 2,
    'a': 1,
    'm': 2,
    'i': 2,
    'n': 2,
    's': 1,
    'f': 1,
    'u': 1
}

TESTE 03:
Texto fornecido: "testing 123321"
Resultado esperado:
{
    't': 2,
    'e': 1,
    's': 1,
    'i': 1,
    'n': 1,
    'g': 1
}

Você pode fazer outros testes caso ache necessário.
"""
#resolução:

def contar_letras(texto):
    # Remova espaços, pontuações, números e caracteres especiais
    texto = ''.join(e for e in texto if e.isalpha())
    # Converta todas as letras para minúsculas
    texto = texto.lower()
    # Crie um dicionário vazio para armazenar a frequência de cada letra
    freq_letras = {}
    # Itere sobre cada caractere no texto
    for char in texto:
        # Verifique se o caractere é uma letra
        if char.isalpha():
            # Se a letra já estiver no dicionário, incremente sua contagem
            if char in freq_letras:
                freq_letras[char] += 1
            # Se a letra não estiver no dicionário, adicione-a com uma contagem de 1
            else:
                freq_letras[char] = 1
    # Retorne o dicionário de frequência de letras
    return freq_letras

# Solicite ao usuário que digite um texto
texto = input("Digite o texto: ")

# Chame a função contar_letras para obter a frequência de cada letra
freq_letras = contar_letras(texto)

# Imprima a frequência de cada letra
for letra, freq in freq_letras.items():
    print(f"{letra}: {freq}")
