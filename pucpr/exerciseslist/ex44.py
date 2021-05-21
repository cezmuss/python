# Lista de Exercícios
# Exercício 44

# Definição das listas
possiveis_votos = [1, 2, 3, 4, 5, 6]
candidatos = ['Tiro Gomas', 'Jair Bonaro', 'João Amedo', 'Lula Molusco', 'Nulo', 'Branco']
votos = []

# Entrada de dados
voto = True
n_votos = 1
while voto != 0:
    print(f"Voto n°{n_votos}")
    voto = int(input("Digite o seu voto: "))
    if voto == 0:
        break
    else:
        while voto not in possiveis_votos:
            print("[Voto invalido.]")
            voto = int(input("Digite o seu voto: "))
        votos.append(voto)
    n_votos += 1

# Imprime votos para o candidato x
contador = 0
for i in range(len(candidatos)):
    print("Votos para ", candidatos[contador], end=" : ")
    if votos.count == 0:
        print("0")
        contador += 1
    else:
        print(votos.count(contador + 1))
        contador += 1

# Calcula a porcentagem de votos nulos e brancos e imprime
porcentagem_nulo = (votos.count(5) / len(votos)) * 100
porcentagem_branco = (votos.count(6) / len(votos)) * 100
print(f"Porcentagem votos Nulos: {round(porcentagem_nulo, 2)}%\n"
      f"Porcentagem votos Brancos: {round(porcentagem_branco, 2)}%")
