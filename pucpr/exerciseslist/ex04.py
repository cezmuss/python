# Lista de Exercícios
# Exercício 4

# Define anos, e as populações e crescimentos de A e B
popA = 80000
creA = 0.03
popB = 200000
creB = 0.015
anos = 0

# Calcula o crescimento de A e B
while popA < popB:
    popA += popA * creA
    popB += popB * creB
    anos += 1

# Imprime em quanto tempo a populaçaõ de A irá ultrapassar ou igualar a população de B
print(f"A população de A irá ultrapassar ou igualar a população de B em {anos} anos")
