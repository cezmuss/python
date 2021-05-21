# Lista de Exercícios
# Exercício 1

# Pede uma nota e verifica se ela está entre 0 e 10
while True:
    nota = float(input("Digite uma nota: "))
    if nota < 0 or nota > 10:
        print("Nota Inválida")
        print("A nota deve ser um valor entre 0 e 10")
    else:
        # Imprime a nota inseridos
        print(f"Nota Registrada: {nota}")
        break
