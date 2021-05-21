"""
4. Criar um algoritmo que simula o jogo de PAR ou ÍMPAR.
O jogo deve ser disputado entre o usuário e o computador em melhor de três,
ou seja, quem ganhar duas rodadas antes ganha.
O comportamento do computador deve ser completamente randômico.
"""

# Importa randint (n° inteiro aleatório) de random (biblioteca)
from random import randint

# Define o número inicial de vitórias
user_win = 0
comp_win = 0

# Imprime o "menu"
print("Jogo de PAR ou ÍMPAR")
print("-----Melhor de 3-----")

# Pergunta se o jogador será ímpar ou par e limita a duas respostas
while True:
    pi = int(input("Par[0] ou Ímpar[1]? "))
    if pi == 0 or pi == 1:
        break
    else:
        print("Digite 0 para Par e 1 para Ímpar")
        continue

# Pede o número do usuário e limita a entre 0 e 5
while user_win < 2 and comp_win < 2:
    while True:
        jogador = int(input("Digite um valor: "))
        if jogador < 0 or jogador > 5:
            print("Somente são válidos valores entre 0 e 5")
            continue
        else:
            break

    computador = randint(0, 5)  # O computador irá pegar valores aleatórios entre 0 e 5
    resultado = jogador + computador  # Soma o valor do usuário e do computador

    # Imprime os valores que o usuário inseriu, o do computador e a soma dos dois
    print(f"Você jogou {jogador} e o computador {computador}.\nResultado: {resultado}")

    if resultado % 2 == pi:  # Se o resultado tiver resto 0 e jogador ser par ou o resto for 1 e o jogador ser ímpar
        print("Você venceu a rodada!")  # Usuário vence a rodada
        user_win += 1  # Adiciona 1 ao número de vitórias do jogador
        print(f"Você possui {user_win} vitórias")  # Imprime o número de vitórias do jogador
        print(f"O computador possui {comp_win} vitórias")  # Imprime o número de vitórias do computador
        continue
    else:
        print("O computador venceu a rodada!")  # Computador vence a rodada
        comp_win += 1  # Adiciona 1 ao número de vitórias do computador
        print(f"Você possui {user_win} vitórias")  # Imprime o número de vitórias do jogador
        print(f"O computador possui {comp_win} vitórias")  # Imprime o número de vitórias do computador
        continue

if user_win > 1:  # Imprime que o usuário venceu o melhor de 3
    print("Parabéns você VENCEU o jogo!!")
elif comp_win > 1:  # Imprime que o computador venceu o melhor de 3
    print("O computador VENCEU o jogo!!")
