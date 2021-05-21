"""
1. Dada a lista de strings a seguir, ordenar em ordem crescente
tomando por base do último caractere ao primeiro em cada string.
"""

lista = ["mercado", "algoritmo", "casa", "fase", "cafezal"]

# Definição de listas
palavras = []
palavras1 = []

# Inverte as palavras na lista e organiza
for palavra in lista:
    palavras.append(palavra[::-1])
    palavras.sort()

# Inverte as palavras novamente
for palavra in palavras:
        palavras1.append(palavra[::-1])

# Exibe o resultado
print(palavras1)
