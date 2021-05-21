# Lista de Exercícios
# Exercício 46

# Definições
nome_atleta = True
n_atleta = 1

# Entradas, calculos e condição de saída
while nome_atleta != '':
    saltos = []
    print(f"Atleta n°{n_atleta}: ")
    nome_atleta = input("Digite o nome do atleta: ")
    if nome_atleta == '':
        break
    else:
        n_salto = 1
        for i in range(5):
            print(f"Salto n°{n_salto}")
            distancia_salto = float(input("Digite a distancia do salto: "))
            saltos.append(distancia_salto)
            n_salto += 1
        print(f"Atleta: {nome_atleta}")
        n_salto = 1
        count = 0
        for i in range(5):
            print(f"{n_salto}° Salto: {saltos[count]}m")
            n_salto += 1
            count += 1

        # Imprime os resultados
        print(f"Melhor salto: {max(saltos)}m")
        print(f"Pior salto: {min(saltos)}m")

        saltos.remove(max(saltos))
        saltos.remove(min(saltos))
        media = sum(saltos) / len(saltos)
        print("Media dos demais saltos: ".format(round(media, 2)))
        print(f"Reusltado Final: {nome_atleta} --> {round(media, 2)}")
        n_atleta += 1
