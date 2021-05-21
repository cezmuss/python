"""
Exercício Jojo da Forca

Enunciado
- Ter uma lista com palavras (20)
- Sortear uma palavra (ramdon.choice)
- Mostrar para o usuário apenas um gabarito da palavra.
    Ex: "curitiba" => Gabarito: "_ _ _ _ _ _ _ _"
        pessoa disse letra "a"
    Palavra: "curitiba" => Gabarito: "_ _ _ _ _ _ _ a"
- Contar os Erros
- Verificar se a letra errada já foi dita anteriormente, e avisar
- Condição de Vitória e derrota - Número de erros para terminar a partida, acertar a palavra para ganhar
- Perguntar se quer jogar novamente
"""

import random

# Lista contendo as palavras
palavras = ["Abacaxi", "Basquete", "Corrida", "Doidera", "Elefante", "Facista", "Grandioso", "Hipopotomo"]

# Começo definindo a palavra e criando variaveis e listas
palavra = random.choice(palavras).lower()  # Palavra selecionada aleatoriamente toda em minúsculo
a = len(palavra)                           # Pega a quantidade de letras da palavra
erros = 0                                  # Variável da quantidade de erros, iniciando com valor 0, máximo 5
erradas = []                               # Lista que irá conter as palavras erradas
certa = ["_", ] * a                        # Define a quantidade de letras que o usuario precisa descobrir

# Jogo
while True:
    print("Gabarito: ", certa)  # Printa o gabarito atual, quando digitado uma letra correta sera atualizado:
    letra = input("Digite uma letra: ")  # Entrada para digitar uma letra e tentar acertar a palavra
    if letra in certa:                   # Caso a letra já esteja nas corretas, contará como repetida
        print("Letra repetida, por favor digite uma letra nova.")
    elif letra in erradas:               # Caso a letra ja esteja nas erradas, contará como repetida
        print("Letra ja foi usada, por favor digite uma letra nova.")
    else:
        # Caso seja uma letra certa que tenha na palavra
        if letra in palavra:  # Se a letra digitada esteja na palavra
            print("Você acertou uma letra!")
            for x in range(a):  # Verifica todos os espaços da palavra para caso tenha mais de uma letra igual,
                # substituindo as duas.
                if letra == palavra[x]:  # Caso a letra seja igual a letra na posição
                    certa[x] = letra     # Substitui no gabarito
                    x += 1               # Aumenta a posição verificada, ao verificar todas termina
        # Caso seja uma letra errada que não tenha na palavra
        else:
            print("Letra errada")
            erros += 1                           # Adiciona um erro para o jogador
            erradas.append(letra)                # Adiciona a letra errada a lista erradas
            print(f"Letras erradas: {erradas}")  # Printa a lista das letras erradas

    # Verificação de vitoria/derrota
    if erros == 5:  # Caso os erros cheguem a 5 (máximo)
        print("Muitos erros, você perdeu o jogo!")
        print(f"A palavra era: {palavra}")
        # Condição de saída
        con = input("Deseja continuar? [S/N] ").upper()  # O jogador perde e o programa pede se ele deseja continuar
        if letra == "N":  # Se sua resposta for não, o programa vai se encerrar
            break
        else:
            palavra = random.choice(palavras).lower()  # Se for sim, uma nova palavra será definida e as variáveis
            # atualizadas
            a = len(palavra)
            erros = 0
            erradas = []
            certa = ["_", ] * a
    else:
        pass
    if '_' in certa:  # Caso ainda existam letras a serem descobertas continuará executando o programa
        pass

    else:  # Caso já tenha acertado todas as letras, o jogador vence
        print(f"Parabens você venceu o jogo! A palavra era {palavra.title()}!")
        con = input('Deseja continuar? [S/N] ').upper()  # Condição de saída.
        if letra == 'N':                                 # Se a resposta for não o programa se encerrará
            break
        else:  # Se sim, uma nova palavra será definida e as variaveis atualizadas
            palavra = random.choice(palavras).lower()
            a = len(palavra)
            erros = 0
            erradas = []
            certa = ["_", ] * a
