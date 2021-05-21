# Lista de Exercícios
# Exercício 23

# Pede um número, cria uma lista vazia e define "divisoes"
numero = int(input("Digite um número: "))
lista = []
divisoes = -1

# Calcula os números primos até o número inserido
for i in range(numero + 1):
    if i % 2 == 1 and i != 2:
        lista.append(i)
        divisoes += 1
    else:
        divisoes += 1

# Imprime os números primos e o número de divisões executadas
print(f"Números primos até {numero}: {lista}")
print(f"Número de divisões executadas: {divisoes}")
