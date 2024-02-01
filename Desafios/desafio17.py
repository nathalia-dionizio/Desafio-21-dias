
import csv

"""
Desafio Calculadora de Despesas Pessoais

Crie um programa em Python que funcione como uma calculadora de despesas pessoais. O programa deve permitir ao usuário registrar suas despesas diárias, categorizá-las e, em seguida, gerar um resumo das despesas por categoria e o total das despesas de uma data específica.

Quais conhecimentos eu preciso adquirir para resolver este desafio?
Manipulação de Listas e Dicionários: Aprenda a usar listas e dicionários para armazenar e organizar despesas.
Loops e Condições: Utilize loops e estruturas condicionais para criar um menu de opções e permitir que o usuário realize ações específicas.
Persistência de Dados: Explore formas de armazenar as despesas em um arquivo csv para que as informações persistam entre as execuções do programa.
Dica importante
Planeje a estrutura de dados que será usada para armazenar as despesas, incluindo informações como valor, descrição, categoria e data.
Implemente um menu de opções intuitivo para o usuário, permitindo que ele escolha entre registrar uma nova despesa, visualizar um resumo por categoria, visualizar o total de despesas ao escolher uma data e sair do programa.
Utilize loops para permitir que o usuário continue interagindo com o programa até que escolha sair.
Implemente a lógica para calcular os totais de despesas por categoria e por data, usando listas e dicionários para organizar os dados.
Considere a persistência de dados, como salvar as despesas em um arquivo CSV, para que as informações sejam mantidas entre as execuções do programa.
Testes
Após criar o seu código, abra o terminal, vá até a pasta que está seu script, e execute o comando abaixo.

python nome-do-seu-script.py
Você pode então realizar alguns testes em seu script. Execute seu script usando os valores abaixo, para ver se ele se comporta como esperado.

TESTE 01: Registrar uma nova despesa com o valor de 50,50, descrição "Compras de supermercado", categoria "Alimentação" e uma data qualquer.
TESTE 02: Registrar uma nova despesa com o valor de 30,00, descrição "Cinema" e categoria "Entretenimento" e uma data qualquer.
TESTE 03: Registrar uma nova despesa com o valor de 100,00, descrição "Combustível", categoria "Transporte" e uma data já utilizada antes.
TESTE 04: Registrar uma nova despesa com o valor de 65,00, descrição "Compras de frutas", categoria "Alimentação" e uma data qualquer.
TESTE 05: Visualizar um resumo das despesas por categoria.
TESTE 06: Visualizar um resumo das despesas por uma data específica.
TESTE 07: Registrar mais despesas e testar novamente a visualização por categoria e por data.
TESTE 08: Sair do programa. Entrar novamente e ver que os dados continuam lá disponíveis.

"""

#resolução:


despesas = []

while True:
    print("Menu de opções:")
    print("1. Registrar nova despesa")
    print("2. Visualizar resumo por categoria")
    print("3. Visualizar total de despesas por data")
    print("4. Sair do programa")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        valor = float(input("Digite o valor da despesa: "))
        descricao = input("Digite a descrição da despesa: ")
        categoria = input("Digite a categoria da despesa: ")
        data = input("Digite a data da despesa (no formato dd/mm/aaaa): ")

        despesa = {"valor": valor, "descricao": descricao, "categoria": categoria, "data": data}
        despesas.append(despesa)

        print("Despesa registrada com sucesso!")

    elif opcao == "2":
        totais_por_categoria = {}

        for despesa in despesas:
            categoria = despesa["categoria"]
            valor = despesa["valor"]

            if categoria in totais_por_categoria:
                totais_por_categoria[categoria] += valor
            else:
                totais_por_categoria[categoria] = valor

        print("Resumo de despesas por categoria:")

        for categoria, total in totais_por_categoria.items():
            print(f"{categoria}: R$ {total:.2f}")

    elif opcao == "3":
        data = input("Digite a data para visualizar o total de despesas (no formato dd/mm/aaaa): ")

        total_por_data = 0

        for despesa in despesas:
            if despesa["data"] == data:
                total_por_data += despesa["valor"]

        print(f"Total de despesas em {data}: R$ {total_por_data:.2f}")

    elif opcao == "4":
        with open("despesas.csv", "w", newline="") as arquivo_csv:
            escritor_csv = csv.writer(arquivo_csv)
            escritor_csv.writerow(["valor", "descricao", "categoria", "data"])

            for despesa in despesas:
                escritor_csv.writerow([despesa["valor"], despesa["descricao"], despesa["categoria"], despesa["data"]])

        print("Despesas salvas em despesas.csv")

        break

    else:
        print("Opção inválida. Tente novamente.")
