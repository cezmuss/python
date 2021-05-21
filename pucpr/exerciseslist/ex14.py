# Lista de Exercícios
# Exercício 14

# Define a quantidade de números e a quantidade de números pares
numeros = 10
pares = 0

# Pede os números e verifica se eles são par
for x in range(numeros):
    n = int(input("Digite um número: "))
    if n % 2 == 0:
        pares += 1

# Calcula os números ímpares
impares = numeros - pares

# Imprime a quantidade de números pares e ímpares
print(f"Quantidade de Números Pares: {pares}")
print(f"Quantidade de Número Ímpares: {impares}")
