# Lista de Exercícios
# Exercício 5

# Define anos, e o valor inicial para a porcentagem do crescimento de A e B
anos = 0
creAp = 0
creBp = 0

# Pede as populações de A e B e verifica se A é menor que B
while True:
    popA = int(input("Digite a população de A: "))
    popB = int(input("Digite a população de B: "))
    if popA >= popB:
        print("A população de A não pode ser maior nem igual que a população de B")
        # Pede o crescimento de A e B, calcula a porcentagem do crescimento e imprime os dados inseridos
    else:
        creA = float(input("Digite o crescimento de A: "))
        creB = float(input("Digite o crescimento de B: "))
        creAp = creA / 100
        creBp = creB / 100
        print(f"A população de A é: {popA}")
        print(f"A população de B é: {popB}")
        print(f"O Crescimento de A é: {creAp}")
        print(f"O Crescimento de B é: {creBp}")

    # Calcula o crescimento de A e B e imprime o resultado
    while popA < popB:
        popA += popA * creAp
        popB += popB * creBp
        anos += 1
    print(f"A população de A irá ultrapassar ou igualar a população de B em {anos} anos")
    break
