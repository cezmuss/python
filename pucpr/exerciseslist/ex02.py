# Lista de Exercícios
# Exercício 2

nome = input("Digite seu nome: ")  # Pede um nome

# Pede uma senha e verifica se é diferente do nome
while True:
    senha = input("Digite sua senha: ")
    if nome == senha:
        print("Sua senha não pode ser igual seu nome")
    else:
        # Imprime os dados inseridos
        print("Dados Registrados")
        print(f"Nome: {nome}")
        print(f"Senha: {senha}")
        break
