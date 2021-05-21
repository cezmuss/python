# Lista de Exercícios
# Exercício 15

# Pede um número e define "ultimo", "penultimo" e "termo"
num = int(input("Digite qual termo da sequência de Fibonacci deseja encontrar: "))
ultimo = 1
penultimo = 1
termo = 0

# Calcula a sequência de fibonacci e imprime o x° termo
if (num == 1) or (num == 2):
    print("1")
else:
    n = 3
    while n <= num:
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        n += 1
    # Imprime o numero° termo da sequência de Fibonacci
    print(f"O {num}° termo da sequência de Fibonacci é: {termo}")
