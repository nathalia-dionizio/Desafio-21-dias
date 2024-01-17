"""
Desafio Conversor de Unidades

Crie um programa que converta unidades de medida. Para este desafio o foco são as conversões de Quilômetros para Milhas, Milhas para Quilômetros, Metros para Pés, Pés para Metros, Graus Celsius para Fahrenheit e Graus Fahrenheit para Celsius.

Quais conhecimentos eu preciso adquirir para resolver este desafio?
Operações Matemáticas: Reforce o conhecimento em operações matemáticas para realizar a conversão entre as unidades de medida mencionadas.
Input/Output: Pratique receber dados do usuário e mostrar resultados.
Dica importante
Antes de iniciar a conversão, certifique-se de entender a relação entre as unidades de medida que deseja converter. Utilize as taxas de conversão fornecidas para realizar os cálculos corretamente: Quilômetros para Milhas (1 quilômetro = 0,621371 milhas), Milhas para Quilômetros (1 milha = 1,60934 quilômetros), Metros para Pés (1 metro = 3,28084 pés), Pés para Metros (1 pé = 0,3048 metros), Graus Celsius para Fahrenheit (Fahrenheit = Celsius * 9/5 + 32) e Graus Fahrenheit para Celsius (Celsius = (Fahrenheit - 32) * 5/9)
Use operações matemáticas adequadas para realizar a conversão de uma unidade para outra, aplicando as taxas de conversão especificadas.
Ao realizar operações matemáticas, o uso de parênteses ajuda a organizar e priorizar corretamente as operações que devem ser feitas antes. Faça bom uso dos parênteses para evitar erros de cálculo.
Testes
Após criar o seu código, abra o terminal, vá até a pasta que está seu script, e execute o comando abaixo.

python nome-do-seu-script.py
Você pode então realizar alguns testes em seu script. Execute seu script usando os valores abaixo, para ver se ele se comporta como esperado.

TESTE 01: Converter 10 quilômetros para milhas -> Resultado da conversão: 6.21371
TESTE 02: Converter 20 milhas para quilômetros -> Resultado da conversão: 32.1868
TESTE 03: Converter 5 metros para pés -> Resultado da conversão: 16.4042
TESTE 04: Converter 100 pés para metros -> Resultado da conversão: 30.48
TESTE 05: Converter 0 graus Celsius para Fahrenheit -> Resultado da conversão: 32.0
TESTE 06: Converter 42 graus Celsius para Fahrenheit -> Resultado da conversão: 107.6
TESTE 07: Converter -3 graus Celsius para Fahrenheit -> Resultado da conversão: 26.6
TESTE 08: Converter 0 graus Fahrenheit para Celsius -> Resultado da conversão: -17.7778
TESTE 09: Converter 100 graus Fahrenheit para Celsius -> Resultado da conversão: 37.7778
TESTE 10: Converter -11 graus Fahrenheit para Celsius -> Resultado da conversão: -23.8889

"""
#resolução:

print("Escolha uma conversão:")
print("1. Quilômetros para Milhas")
print("2. Milhas para Quilômetros")
print("3. Metros para Pés")
print("4. Pés para Metros")
print("5. Graus Celsius para Fahrenheit")
print("6. Graus Fahrenheit para Celsius")

# Receba a opção do usuário
opcao = int(input("Digite a opção: "))

# Verifique se a opção é válida
if opcao < 1 or opcao > 6:
  print("Opção inválida. Tente novamente.")
else:
  valor = float(input("Digite o valor a ser convertido: "))

  # Faz conversão 
  if opcao == 1:
  # Quilômetros para Milhas
    resultado = valor * 0.621371
    print(f"{valor} quilômetros são {resultado} milhas")
  elif opcao == 2:
  # Milhas para Quilômetros
    resultado = valor * 1.60934
    print(f"{valor} milhas são {resultado} quilômetros")
  elif opcao == 3:
  # Metros para Pés
    resultado = valor * 3.28084
    print(f"{valor} metros são {resultado} pés")
  elif opcao == 4:
  # Pés para Metros
    resultado = valor * 0.3048
    print(f"{valor} pés são {resultado} metros")
  elif opcao == 5:
  # Graus Celsius para Fahrenheit
    resultado = valor * 9/5 + 32
    print(f"{valor} graus Celsius são {resultado} graus Fahrenheit")
  elif opcao == 6:
  # Graus Fahrenheit para Celsius
    resultado = (valor - 32) * 5/9
    print(f"{valor} graus Fahrenheit são {resultado} graus Celsius")
