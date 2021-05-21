# Lista de Exercícios
# Exercício 33

# Pede um número para um quantidade, cria uma lista vazia e define "n_temp2"
n_temp = int(input("Quantidade de temperaturas que irá digitar: "))
temperaturas = []
n_temp2 = 1

# Pede quantidade números
for i in range(n_temp):
    temp = temperaturas.append(float(input(f"Digite a {n_temp2}° temperatura: ")))
    n_temp2 += 1

# Imprime a maior, a menor e média das temperaturas
print(f"Maior temperatura: {max(temperaturas)}")
print(f"Menor temperatura: {min(temperaturas)}")
print(f"Média: {round(sum(temperaturas) / len(temperaturas), 2)}")
