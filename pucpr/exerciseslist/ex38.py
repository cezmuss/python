# Lista de Exercícios
# Exercício 38

# Pede o salário e define o aumento do salario
salario = float(input("Digite o salário inicial do funcionario: "))
aumento = 1.5

# Calcula e imprime o aumento do salario
for i in range(1996, 2020 + 1):
    salario_atual = salario + (salario * (aumento / 100))
    aumento = aumento * 2
    print(f"Salário em {i}: {salario_atual:2}")
