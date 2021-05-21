# Lista de Exercícios
# Exercício 8

# Pede um primeiro número e define o valor inicial de "soma"
numero = int(input("Digite um 1° número: "))
soma = numero

# Pede outros 4 números e calcula a soma de todos
for n in range(2, 6):
    num = int(input(f"Digite um {n}° número: "))
    soma += num

# Calcula a média dos 5 números inseridos
media = soma / 5

# Imprime a soma e a média dos 5 números
print(f"A Soma dos 5 número é igual a: {soma}")
print(f"A Media dos 5 número é igual a: {media:2}")
