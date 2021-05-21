# Lista de Exercícios
# Exercício 32

# Pede um número e define "c" e "f"
numero = int(input("Digite um número para descobrir seu fatorial: "))
c = numero
f = 1

# Calcula e imprime o fatorial
print(f"{numero}! = ", end='')
while c > 0:
    print(f"{c}", end='')
    print(" . " if c > 1 else " = ", end='')
    f *= c
    c -= 1
print(f"{f}")
