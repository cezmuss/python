# Lista de Exercícios
# Exercício 35

# Pede um número e cria uma lista vazia
numero = int(input("Digite um número para ver os números primos até ele: "))
lista = []

# Calcula os números primos e os adiciona em na lista
for i in range(numero + 1):
    if i % 2 == 1 and i != 2:
        lista.append(i)

# Imprime a quantidade e quais são os números primos
print(f"Números primos até {numero}: {lista}")
print(f"Quantidade de números primos até {numero}: {len(lista)}")
