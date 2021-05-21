# Lista de Exercícios
# Exercício 24

# Pede um número para quantidade e verifica se está entre 2 e 10
while True:
    quant = int(input("Digite quantas notas para saber a média delas: "))
    if quant < 2 or quant > 10:
        print("Mínimo: 2\nMáximo: 10")
        continue
    else:
        break

# Pede uma primeira nota e verifica se está entre 0 e 10
while True:
    nota = float(input("Digite a 1° nota: "))
    if nota < 0 or nota > 10:
        print("Nota Mínima: 0\nNota Máxima: 10")
        continue
    else:
        break

# Define "soma"
soma = nota

# Pede as outras notas, verifica se estão entre 0 e 10 e soma todas
for i in range(2, quant + 1):
    while True:
        nota = float(input(f"Digite a {i}° nota: "))
        if nota < 0 or nota > 10:
            print("Nota Mínima: 0\nNota Máxima: 10")
            continue
        else:
            i += 1
            soma += nota
            break

# Calcula e imprime a média
media = soma / quant
print(f"A média das {quant} notas é igual a: {media:1}")
