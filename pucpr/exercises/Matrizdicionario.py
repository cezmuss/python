# Fazer uma matriz identidade utilizando dicionários

matriz = {}

for i in range(3):
    matriz[i] = {}
    for j in range(3):
        if i == j:
            matriz[i][j] = 1
        else:
            matriz[i][j] = 2

print(matriz)
