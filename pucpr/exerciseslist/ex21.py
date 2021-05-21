# Lista de Exercícios
# Exercício 21

# Pede um número e verifica se ele é maior que 1
while True:
    num = int(input("Digite um número para verificar se ele é primo: "))
    if num < 2:
        print("Somente são válidos números maiores que 1")
        continue
    else:
        break

# Define "cont" e "i"
cont = 0
i = 0

# Verifica se o número é primo
while i <= num or cont < 2:
    i += 1
    x = num % i
    if x == 0:
        cont += 1

# Imprime se o número é primo ou não
if cont <= 2:
    print(f"O Número {num} é primo")
else:
    print(f"O Número {num} não é primo")
