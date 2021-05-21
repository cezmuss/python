# Lista de Exercícios
# Exercício 20

# Pede um número e verifica se está entre 0 e 16
while True:
    while True:
        num = int(input("Digite um número para saber seu fatorial: "))
        if num < 0 or num > 16:
            print("Somente são válidos valores entre 0 e 16")
        else:
            break

    # Define "result" e "n"
    result = 1
    n = 1

    # Calcula o fatorial
    while n <= num:
        result *= n
        n += 1

    # Imprime o resultado
    print(f"O fatorial de {num} é: {result}")
    reset = input("Digite 0 para reiniciar ou 1 para encerrar: ")
    # Condição de saída
    if reset == "0":
        continue
    else:
        print("Finalizando Programa")
        break
