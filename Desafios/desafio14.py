import random
import string

"""
Desafio Gerador de Senhas

Desenvolva um programa que seja capaz de gerar senhas aleatórias com critérios especificados pelo usuário, como comprimento e inclusão de números, letras maiúsculas, letras minúsculas e caracteres especiais.

Quais conhecimentos eu preciso adquirir para resolver este desafio?
Manipulação de Strings: Aprenda a criar, concatenar e manipular strings.
Geração de Números Aleatórios: Utilize o módulo random para gerar caracteres aleatórios.
Input e Output: Receba as preferências do usuário e exiba a senha gerada.
Dica importante
Planeje como você irá criar as senhas de acordo com os critérios fornecidos pelo usuário, considerando o comprimento desejado e a inclusão de números, letras maiúsculas, letras minúsculas e caracteres especiais.
Utilize o módulo random para gerar caracteres aleatórios de forma imprevisível.
Lembre-se de garantir que a senha gerada atenda aos critérios especificados pelo usuário.
Testes
Após criar o seu código, abra o terminal, vá até a pasta que está seu script, e execute o comando abaixo.

python nome-do-seu-script.py
Você pode então realizar alguns testes em seu script. Execute seu script usando os valores abaixo, para ver se ele se comporta como esperado.

TESTE 01: Gerar uma senha de comprimento 8 com números e caracteres especiais, mas sem letras maiúsculas e letras minúsculas.
TESTE 02: Gerar uma senha de comprimento 12 com números, mas sem letras maiúsculas, letras minúsculas ou caracteres especiais.
TESTE 03: Gerar uma senha de comprimento 16 com letras maiúsculas e números, mas sem letras minúsculas ou caracteres especiais.
TESTE 04: Gerar uma senha de comprimento 20 com letras minúsculas, números e caracteres especiais.
TESTE 05: Gerar uma senha de comprimento 6 com letras maiúsculas, letras minúsculas, números e caracteres especiais.
Você pode fazer outros testes caso ache necessário.
"""
#resolução:

def generate_password(length, uppercase, lowercase, numbers, special_characters):
    # Define the character set based on user's criteria
    character_set = ""
    if uppercase:
        character_set += string.ascii_uppercase
    if lowercase:
        character_set += string.ascii_lowercase
    if numbers:
        character_set += string.digits
    if special_characters:
        character_set += string.punctuation

    # Generate the password
    password = "".join(random.choice(character_set) for i in range(length))
    return password

# Prompt the user for password criteria
length = int(input("Qual o comprimento da senha desejada? "))
uppercase = input("Incluir letras maiúsculas? (s/n) ").lower() == "s"
lowercase = input("Incluir letras minúsculas? (s/n) ").lower() == "s"
numbers = input("Incluir números? (s/n) ").lower() == "s"
special_characters = input("Incluir caracteres especiais? (s/n) ").lower() == "s"

# Generate the password based on user's criteria
password = generate_password(length, uppercase, lowercase, numbers, special_characters)
print(f"Sua senha gerada é: **{password}**")
