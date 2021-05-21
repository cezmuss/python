# Lista de Exercícios
# Exercício 47

# Definições
import time
nome_atleta = True
n_atleta = 1

# Entradas, calculos e condição de saída
while nome_atleta != '':
    notas = []
    print(f"Atleta n°{n_atleta}")
    nome_atleta = input("Digite o nome do atleta: ")
    if nome_atleta == '':
        break
    else:
        n_jurado = 1
        for i in range(7):
            print(f"Jurado n°{n_jurado}")
            nota = float(input("Digite a nota: "))
            notas.append(nota)
            n_jurado += 1
        print(f"Atleta: {nome_atleta}")
        n_jurado = 1
        count = 0
        for i in range(7):
            print(f"{n_jurado}° Jurado: {notas[count]}")
            n_jurado += 1
            count += 1

        # Imprime os resultados
        print("Resultado Final")
        print(f"Nome do atleta: {nome_atleta}")
        print(f"Melhor nota: {max(notas)}")
        print(f"Pior nota: {min(notas)}")
        notas.remove(max(notas))
        notas.remove(min(notas))
        media = sum(notas) / len(notas)
        print(f"Media: {round(media, 2)}")
        n_atleta += 1
        print("Reiniciando em 5 segundos")
        time.sleep(5)
