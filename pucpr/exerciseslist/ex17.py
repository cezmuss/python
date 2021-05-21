# Lista de Exercícios
# Exercício 17

# Pede um número e define "resultado" e "n"
num = int(input("Digite um número para saber seu fatorial: "))
resultado = 1
n = 1

# Calcula o fatorial e imprime o resultado
while n <= num:
    resultado *= n
    n += 1

# Imprime o resultado
print(f"O fatorial de {num} é: {resultado}")
