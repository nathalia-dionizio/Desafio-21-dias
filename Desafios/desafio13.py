import re

"""
Desafio Validador de E-mail

Quais conhecimentos eu preciso adquirir para resolver este desafio?
Expressões Regulares (Regex): Aprenda a usar expressões regulares em Python para validar formatos de e-mail.
Condições e Manipulação de Strings: Use condições para verificar a validade.
Dica importante
Pesquise sobre expressões regulares em Python, pois são essenciais para validar e-mails com precisão.
Considere os elementos abaixo para considerar um e-mail válido:
O endereço de e-mail deve conter um único símbolo "@" que separa a parte local e o domínio.
A parte local (antes do "@") deve consistir em letras maiúsculas e minúsculas, dígitos e alguns caracteres especiais como ".", "_", "%", "+", e "-".
O domínio (após o "@") deve ser composto por letras maiúsculas e minúsculas, dígitos e os caracteres especiais ".", e "-".
O domínio deve ter pelo menos um ponto "." para separar o domínio de alto nível (TLD) do domínio de segundo nível (SLD), como em "exemplo.com".
O TLD (Top-Level Domain) deve consistir de pelo menos duas letras maiúsculas ou minúsculas.
Os espaços em branco não são permitidos em um endereço de e-mail.
Testes
Após criar o seu código, abra o terminal, vá até a pasta que está seu script, e execute o comando abaixo.

python nome-do-seu-script.py
Você pode então realizar alguns testes em seu script. Execute seu script usando os valores abaixo, para ver se ele se comporta como esperado.

TESTE 01:
E-mail fornecido: "usuario@email.com"
Resultado esperado: E-mail válido

TESTE 02:
E-mail fornecido: "email.com"
Resultado esperado: E-mail inválido

TESTE 03:
E-mail fornecido: "usuario@.com"
Resultado esperado: E-mail inválido

TESTE 04:
E-mail fornecido: "usuario@dominio"
Resultado esperado: E-mail inválido

TESTE 05:
E-mail fornecido: "@dominio.com"
Resultado esperado: E-mail inválido

TESTE 06:
E-mail fornecido: "meu email@dominio.com"
Resultado esperado: E-mail inválido

TESTE 07:
E-mail fornecido: "meu@dominio.c"
Resultado esperado: E-mail inválido
Você pode fazer outros testes caso ache necessário.
"""
#resolução:

def is_valid_email(email):
    # Verifica se o email contém apenas um símbolo "@"
    if email.count('@') != 1:
        return False

    # Separa o email em parte local e parte do domínio
    local_part, domain_part = email.split('@')

    # Verifica se ambas as partes não estão vazias
    if len(local_part) == 0 or len(domain_part) == 0:
        return False

    # Verifica se a parte local contém apenas letras, dígitos e alguns caracteres especiais
    local_regex = r'^[A-Za-z0-9._%+-]+$'
    if not re.match(local_regex, local_part):
        return False

    # Verifica se a parte do domínio contém apenas letras, dígitos e alguns caracteres especiais
    domain_regex = r'^[A-Za-z0-9.-]+$'
    if not re.match(domain_regex, domain_part):
        return False

    # Verifica se a parte do domínio tem pelo menos um "." para separar o TLD do SLD
    if '.' not in domain_part:
        return False

    # Separa a parte do domínio em TLD e SLD
    tld, sld = domain_part.rsplit('.', 1)

    # Verifica se o TLD tem pelo menos duas letras
    if len(tld) < 2:
        return False

    # Verifica se há pelo menos um ponto no SLD
    if len(sld) < 1:
        return False

    return True

# Solicita ao usuário que digite o endereço de e-mail
email = input("Digite o endereço de e-mail: ")

# Verifica se o endereço de e-mail é válido ou não
if is_valid_email(email):
    print(f"{email} é um endereço de e-mail válido.")
else:
    print(f"{email} não é um endereço de e-mail válido.")

