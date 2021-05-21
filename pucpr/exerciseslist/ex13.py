# Lista de Exercícios
# Exercício 13

# Pede um número para a base e um para o expoente
base = int(input("Digite um valor para a base: "))
expoente = int(input("Digite um valor para o expoente: "))

potencia = 1  # Define "potencia"

# Calcula a base elevado ao expoente inseridos
for n in range(expoente):
    potencia *= base
    n += 1

# Imprime o resultado
print(f"O número {base} elevado por {expoente} é igual a: {potencia}")
