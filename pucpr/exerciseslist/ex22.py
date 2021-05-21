# Lista de Exercícios
# Exercício 22

# Pede um número e cria uma lista vazia
num = int(input("Digite um número: "))
lista = []

# Verifica se o número é primo ou não, se primo imprime que o número é primo
if num % 2 != 0 or num == 2:
    print(f"O número {num} é primo")
else:
    for i in range(num):
        if num % (i + 1) == 0:
            lista.append(i + 1)
    # Se não for primo imprime que não é primo e seus divisores
    print(f"Esse número não é primo e seus divisores são: {lista}")
