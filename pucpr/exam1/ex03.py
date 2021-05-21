"""
3. No quadrangular final da Copa Xurupita quatro times jogam entre si
para definir quem é o time campeão. A fim de facilitar a vida dos organizadores,
elabore um algoritmo que solicita as seguintes informações:
- O nome de cada time
- O placar de cada um dos jogos
Levar em consideração que:
- Cada vitória vale 3 pontos
- Cada empate vale 1 ponto
- Cada derrota não vale ponto
Ao final, o algoritmo deve mostrar, para cada time:
- Número de vitórias
- Número de pontos
- Saldo de gols
- Quantos gols fez
"""

# Definições
a = 0
b = 4
dtimes = {}
ltimes = []

# Abre laço pedindo o nome de 4 times
for x in range(1, 5):
    times = input(f"Qual o nome do {x}º time: ")
    # Adiciona a quantidade de vitórias, pontos, saldo e gols para cada time no dicionário
    dtimes[times] = {"Vitórias": 0, "Pontos": 0, "Saldo de gols": 0, "Gols": 0}
    ltimes.append(times)  # Adiciona o nome dos times em uma lista
    print(ltimes)  # Imprime a lista contendo o nome dos times

for x in ltimes:  # Abre laço que irá rodar o mesmo que a quantidade de times
    for y in range(a + 1, b):  # Abre laço contendo os jogos
        print("Digite o resultado de {} X {}".format(x, ltimes[y]))  # Pede o resultado do jogo
        golsA = int(input(f"Gols do {x}: "))                         # Pede os gols do primeiro time
        golsB = int(input(f"Gols do {ltimes[y]}: "))                 # Pede os gols do segundo time
        dtimes[x]["Gols"] += golsA                                   # Adiciona os gols digitados para o time
        dtimes[ltimes[y]]["Gols"] += golsB                           # Adiciona os gols digitados para o outro time
        dtimes[x]["Saldo de gols"] += golsA - golsB                  # Calcula o saldo de gols de um time
        dtimes[ltimes[y]]["Saldo de gols"] += golsB - golsA          # Calcula o saldo de gols de outro time
        if golsA > golsB:                                            # Se o primeiro time ganhar
            dtimes[x]["Vitórias"] += 1                               # Adiciona 1 ao total de vitórias do primeiro time
            dtimes[x]["Pontos"] += 3                                 # Adiciona 3 ao total de pontos do primeiro time
        if golsB > golsA:                                            # Se o segundo time ganhar
            dtimes[ltimes[y]]["Vitórias"] += 1                       # Adiciona 1 ao total de vitórias do segundo time
            dtimes[ltimes[y]]["Pontos"] += 3                         # Adiciona 3 ao total de pontos do segundo time
        if golsA == golsB:                                           # Se os dois empatarem
            dtimes[x]["Pontos"] += 1                                 # Adiciona 1 a quantidade de pontos dos dois times
            dtimes[ltimes[y]]["Pontos"] += 1                         # Adiciona 1 a quantidade de pontos dos dois times
        else:                                                        # Caso nenhuma das condições acima sejam verdadeira
            continue                                                 # Recomeça o loop

print(dtimes)  # Imprime os dados pedidos
