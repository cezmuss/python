# Lista de Exercícios
# Exercício 27

# Define "soma"
soma = 0

# Pede um número para uma quantidade e verifica se está entre 2 e 15
while True:
    turmas = int(input("Digite uma quantidade de turmas: "))
    if turmas < 2 or turmas > 15:
        print("Mínimo de turmas: 2\nMáximo de turmas: 15")
        continue
    else:
        break

# Pede o número de alunos por turma, verifica se está entre 0 e 40 e calcula a soma dos valores
for n in range(turmas):
    while True:
        alunos = int(input("Digite a quantidade de alunos por turma: "))
        if alunos < 0 or alunos > 40:
            print("Mínimo de alunos: 0\nMáximo de alunos: 40")
            continue
        else:
            n += 1
            soma += alunos
            break

# Calcula e imprime a média
media = soma / turmas

print(f"A média de Alunos das {turmas} turmas é igual a: {media:2}")
