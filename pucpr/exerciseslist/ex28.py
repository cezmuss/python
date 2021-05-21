# Lista de Exercícios
# Exercício 28

# Pede um número para um a quantidade e verifica se está entre 2 e 15
while True:
    qcd = int(input("Digite a quantidade de CD's da coleção: "))
    if qcd < 2 or qcd > 15:
        print("Mínimo de CD's: 2\nMáximo de CD's: 15")
        continue
    else:
        break

# Pede o preço dos cd's e verifica se está entre 0 e 1000
while True:
    pc1d = float(input("Digite o preço do 1° CD: "))
    if pc1d < 0 or pc1d > 1000:
        print("Valor Mínimo: 0\nValor Máximo: 1000")
        continue
    else:
        break

# Define "soma"
soma = pc1d

# Pede o restante dos números, verifica se está entre 0 e 1000 e calcula a soma dos valores
for n in range(2, qcd + 1):
    while True:
        pcd = float(input("Digite o preço do {}° CD: ".format(n)))
        if pcd < 0 or pcd > 1000:
            print("Valor Mínimo: 0\nValor Máximo: 1000")
            continue
        else:
            n += 1
            soma += pcd
            break

# Calcula e imprime a média de preço dos cd's, além do total investido
media = soma / qcd

print(f"A média de preço dos {qcd} CD's é igual a: {media:2}")
print(f"O valor total investido foi igual a: {soma:2}")
