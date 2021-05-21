# Lista de Exercícios
# Exercício 19

# Pede uma quantidade e verifica se está entre 0 e 15
while True:
    quant = int(input("Digite uma quantidade: "))
    if quant < 0 or quant > 15:
        print("Quantidade mínima: 0\nQuantidade máxima: 15")
    else:
        break

# Pede um primeiro número e verifica se está entre 0 e 1000
while True:
    prim = int(input("Digite o 1° número: "))
    if prim < 0 or prim > 1000:
        print("Somente são válidos valores entre 0 e 1000")
    else:
        break

# Define "maior", "menor", "soma" e "n"
maior = prim
menor = prim
soma = prim
n = 1

# Pede o restante dos números e verifica se estão entre 0 e 1000
while n < quant:
    n += 1
    while True:
        num = int(input(f"Digite o {n}° número: "))
        if num < 0 or num > 1000:
            print("Somente são válidos valores entre 0 e 1000")
        else:
            break
    # Calcula a soma, o maior e menor número
    soma += num
    if num > maior:
        maior = num
    if num < menor:
        menor = num

# Imprime a soma, o maior e menor de todos os números inseridos
print(f"A soma dos {quant} valores é igual a: {soma}")
print(f"O maior dos {quant} valores é igual a: {maior}")
print(f"O menor dos {quant} valores é igual a: {menor}")
