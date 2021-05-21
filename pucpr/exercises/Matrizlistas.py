# Fazer uma matriz identidade utilizando listas

matriz = []

for i in range(3):
    matriz.append([])
    for j in range(3):
        if i == j:
            matriz[i].append(1)
        else:
            matriz[i].append(0)

print(matriz)

for i in range(3):
    linha = ""
    for j in range(3):
        linha += "%d " % matriz[i][j]
    print(linha)

#            i: 0      i: 0  i: 0     i: 0
#            j: 0      j: 0  j: 1     j: 2
# matriz[i][j]: n [[]] [[1]] [[1, 0]] [[1, 0, 0]]

# i: 1         i: 1          i: 1           i: 1
# j: 0         j: 0          j: 1           j: 2
# [[1,0,0],[]] [[1,0,0],[0]] [1,0,0],[0,1]] [[1,0,0],[0,1,0]]

# i: 2                  i: 2                  i: 2                   i: 2
# j: 0                  j: 0                  j: 1                   j: 2
# [[1,0,0],[0,1,0], []] [[1,0,0],[0,1,0],[0]] [1,0,0],[0,1,0],[0,0]] [[1,0,0],[0,1,0],[0,0,1]]
