# Lista de Exercícios
# Exercício 11

# Pede dois números e os cria uma lista contendo os dois números
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
lista = [num1, num2]
i = 0
# Calcula a soma dos valores do intervalo dos dois números e imprime o intervalo e a soma
if num1 < num2:
    for n in list(range(num1, num2)):
        lista.append(n)
        i += n
        print(i)
    print(f"Intervalo entre {num1} e {num2}: {lista[3:]}")
    print(f"Soma: {i - num1}")
# Calcula a soma dos valores do intervalo dos dois números e imprime o intervalo e a soma
if num1 > num2:
    for n in list(range(num2, num1)):
        lista.append(n)
        i += n
        print(i)
    lista.reverse()
    # Imprime o intervalo dos dois números e a soma dos números do intervalo
    print(f"Intervalo entre {num1} e {num2}: {lista[:-3]}")
    print(f"Soma: {i - num2}")
