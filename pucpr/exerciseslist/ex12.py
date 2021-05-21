# Lista de Exercícios
# Exercício 12

# Pede um número e verifica se está entre 1 e 10
while True:
    numero = int(input("Digite um número para ver sua tabuada: "))
    if numero < 1 or numero > 10:
        print("O número deve ser entre 1 e 10")
    else:
        # Calcula e imprime a tabuada do número inserido
        print("Tabuada de {}:".format(numero))
        for n in range(1, 11):
            print(f"{numero} X {n:2} = {numero * n}")
        break
