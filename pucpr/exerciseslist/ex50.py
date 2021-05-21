# Lista de Exercícios
# Exercício 50

# Definições
h = 1
n = 2
h_lista = []
n_lista = []

# Cálculos
print("H = 1 +", end="")

while n <= 10 - 1:
    print(" ", h, "/", n, " + ", end="")
    h_lista.append(h)
    n_lista.append(n)
    n += 1

# Imprime o resultado
print(f"{h}/{n} => {sum(h_lista)}/{sum(n_lista)} => {round(sum(h_lista) / sum(n_lista))}")
