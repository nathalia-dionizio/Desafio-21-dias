"""
Desafio Calculadora Básica
Desenvolva um programa que realize operações básicas de matemática, como adição, subtração, multiplicação e divisão.

Quais conhecimentos eu preciso adquirir para resolver este desafio?
Operações Matemáticas em Python: Conheça como realizar operações matemáticas básicas usando os operadores +, -, * e /.
Input e Output: Aprenda a receber entrada do usuário usando input() e mostrar resultados.
Dica importante
Você pode se deparar com um erro ao tentar usar o valor inserido pelo usuário na operação matemática... Tudo que o usuário insere vem como String, então, para fazer adição, subtração, multiplicação e divisão do número recebido, você vai precisar converter a String recebida para um inteiro ou para float (se quiser que sua calculadora faça contas com números decimais).
Lembre-se que float em Python é utilizando . e não , (2.5 e não 2,5). Você pode fazer um tratamento extra no seu código se quiser evitar que o uso da , cause um erro de código, mas faça apenas se quiser tentar algo a mais, para o desafio não é necessário.
Você pode fazer alguns tratamentos para lidar com casos do tipo divisão por 0.
Testes
Após criar o seu código, abra o terminal, vá até a pasta que está seu script, e execute o comando abaixo.

python nome-do-seu-script.py
Você pode então realizar alguns testes em seu script. Execute seu script várias vezes para ver se ele se comporta como esperado para cada um dos valores abaixo:

TESTE 01: 1 + 5 -> 6
TESTE 02: 5 - 1 -> 4
TESTE 03: 2 x 30 -> 60
TESTE 04: 21 / 7 -> 3
TESTE 05: 10 / 0 -> Não é possível dividir por zero
TESTE 06: 1 + -5 -> -4
TESTE 07: 5 - -1 -> 6
TESTE 08: 2 x -30 -> -60
TESTE 09: -21 / 7 -> -3
TESTE 10: -10 / 0 -> Não é possível dividir por zero
"""

#resolução:

operacao = int(input("Digite o número da operação que deseja: 1 adição, 2 subtração, 3 multiplicação ou 4 divisão?"))
numeroUm = int(input("Digite o primeiro número da sua operação"))
numeroDois = int(input("Digite o segundo número da sua operação"))

if operacao == 1: 
  print(f"Resultado:{numeroUm + numeroDois}")
elif operacao == 2: 
  print(f"Resultado:{numeroUm - numeroDois}")
elif operacao == 3: 
  print(f"Resultado:{numeroUm * numeroDois}")
else: 
  try:
    resultado = numeroUm // numeroDois
  except ZeroDivisionError:
    resultado = 0
  print(f"Resultado:{resultado}")