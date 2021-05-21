# Lista de Exercícios
# Exercício 36

# Pede 3 números
n_tabuada = int(input("Digite um número para descobrir sua tabuada: "))
n_inicial = int(input("Iniciar a tabuada no: "))
n_final = int(input("Finalizar a tabuada no: "))

# Define "result"
result = n_inicial

# Imprime a tabuada
print(f"Vou montar a tabuada de {n_tabuada} começando em {n_inicial} e terminando em {n_final}:")
for i in range(n_inicial, n_final + 1):
    print(f"{n_tabuada} X {result:2} = {n_tabuada * result}")
    result += 1
