# Lista de Exercícios
# Exercício 7

maior = -99999  # Define o valor de inicial "maior"

# Pede um número 5 vezes
for n in range(5):
    numero = float(input("Informe um número: "))
    if numero > maior:
        maior = numero

# Imprime o maior dos 5 números inseridos
print(f"O maior dos 5 números é: {maior}")
