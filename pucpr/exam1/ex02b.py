"""
2b. Dada a lista a seguir, com registros do número de vendas
por mês e cidade [mês, cidade, vendas], elaborar um algoritmo
que cria um dicionário que totaliza vendas por cidade.
Ou seja, a chave é a cidade, cujo valor é o total de vendas da lista naquela cidade.
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
vendas_city = {}

# Alimenta o dicionário com os dados
for item in dados:
    if item[1] in vendas_city:
        vendas_city[item[1]] += item[2]
    else:
        vendas_city[item[1]] = item[2]

# Exibe os resultados
print("Relatório de vendas por cidade: ")
print(vendas_city)
