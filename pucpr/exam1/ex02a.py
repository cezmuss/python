"""
2a. Dada a lista a seguir, com registros do número de vendas
por mês e cidade [mês, cidade, vendas], elaborar um algoritmo
que cria um dicionário que totaliza vendas por mês.
Ou seja, a chave é o mês, cujo valor é o total de vendas da lista naquele mês.
"""

dados = [
    ["Fevereiro", "Curitiba", 30],
    ["Maio", "Londrina", 27],
    ["Janeiro", "Curitiba", 48],
    ["Maio", "Curitiba", 32],
    ["Maio", "Astorga", 12],
    ["Fevereiro", "Astorga", 15],
    ["Fevereiro", "Londrina", 41],
    ["Janeiro", "Londrina", 22]
]

# Criação do dicionário
vendas_mes = {}

# Alimenta o dicionário com os dados
for item in dados:
    if item[0] in vendas_mes:
        vendas_mes[item[0]] += item[2]
    else:
        vendas_mes[item[0]] = item[2]

# Exibe os resultados
print("Relatório de vendas por mês: ")
print(vendas_mes)
