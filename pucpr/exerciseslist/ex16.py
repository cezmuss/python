# Lista de Exercícios
# Exercício 16

# Define "ultimo", "penultimo" e "termo"
ultimo = 1
penultimo = 1
print(ultimo)
print(penultimo)
termo = 0

# Calcula e imprime a sequencia de fibonacci até 500
while termo < 500:
    termo = ultimo + penultimo
    penultimo = ultimo
    ultimo = termo
    if termo < 500:
        print(termo)
    else:
        print("O proximo termo será maior que 500")
