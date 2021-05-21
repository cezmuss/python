# Lista de Exercícios
# Exercício 26

# Define "c1", "c2" e "c3"
c1 = 0
c2 = 0
c3 = 0

# Pede um número para uma quantidade e verifica se está acima de 3
while True:
    eleitores = int(input("Digite a quantidade de eleitores: "))
    if eleitores < 3:
        print("O mínimo de eleitores é 3")
        continue
    else:
        break

# Pede qual o voto e calcula a quantidade de votos para cada candidato
for n in range(eleitores):
    while True:
        voto = int(input("Vote em 1, 2, ou 3: "))
        if voto == 1:
            c1 += 1
            break
        elif voto == 2:
            c2 += 1
            break
        elif voto == 3:
            c3 += 1
            break
        else:
            print("Voto Inválido")
            continue

# Imprime a quantidade de votos de cada candidato
print(f"Quantidade de votos do Candidato 1: {c1}")
print(f"Quantidade de votos do Candidato 2: {c2}")
print(f"Quantidade de votos do Candidato 3: {c3}")
