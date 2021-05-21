# Lista de Exercícios
# Exercício 25

# Pede um número para quantidade e verifica se está entre 2 e 10
while True:
    quant = int(input("Digite uma quantidade de pessoas: "))
    if quant < 2 or quant > 25:
        print("Mínimo: 2\nMáximo: 25")
        continue
    else:
        break

# Pede uma primeira nota e verifica se está entre 0 e 10
while True:
    idade = int(input("Digite a idade da 1° pessoa: "))
    if idade < 0 or idade > 150:
        print("Idade Mínima: 0\nIdade Máxima: 150")
        continue
    else:
        break

# Define "soma"
soma = idade

# Pede as outras notas, verifica se estão entre 0 e 10 e soma todas
for i in range(2, quant + 1):
    while True:
        idade = int(input(f"Digite a idade da {i}° pessoa: "))
        if idade < 0 or idade > 150:
            print("Idade Mínima: 0\nIdade Máxima: 150")
            continue
        else:
            i += 1
            soma += idade
            break

# Calcula a média e imprime
media = soma / quant

print(f"A média das {quant} idades é igual a: {media:1}")

# Imprime em qual grupo a média de idades está
if 0 <= media <= 25:
    print("O Grupo de pessoas é considerado como um grupo jovem")
elif 26 <= media <= 60:
    print("O Grupo de pessoas é considerado como um grupo adulto")
elif media > 60:
    print("O Grupo de pessoas é considerado um grupo idoso")
