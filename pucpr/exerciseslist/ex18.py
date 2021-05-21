# Lista de Exercícios
# Exercício 18

# Pede um quantidade, um primeiro número, define "n", "soma" e cria uma lista contendo o primeiro número
quant = int(input("Digite uma quantidade: "))
prim = int(input("Digite o 1° número: "))
n = 1
soma = prim
lista = [prim]

# Pede o restante dos números e os adiciona na lista
while n < quant:
    num = int(input(f"Digite o {n}° número: "))
    n += 1
    soma += num
    lista.append(num)

# Imprime a soma, o maior e o menor dos números inseridos
print(f"A soma dos {quant} valores é igual a: {soma}")
print(f"O maior dos {quant} valores é igual a: {max(lista)}")
print(f"O menor dos {quant} valores é igual a: {min(lista)}")
