# Lista de Exercícios
# Exercício 3

# Pede o nome do usuário e verifica se possui mais de 4 caracteres
nome = input("Digite seu nome: ")
while len(nome) < 4:
    print("Nome Inválido")
    nome = input("Digite seu nome novamente: ")

# Pede a idade do usuário e verifica se está entre 0 e 150
idade = int(input("Digite sua idade: "))
while idade < 0 or idade > 150:
    print("Idade Inválida")
    idade = int(input("Digite sua idade novamente: "))

# Pede o salário do usuário e verifica se é maior que 0
salario = int(input("Digite seu salário: "))
while salario < 0:
    print("Salário Inválido")
    salario = float(input("Digite seu salário novamente: "))

# Pede o sexo do usuário e verifica se é "f" ou "m"
sexo = input("Digite seu sexo:\nf - Feminino\nm - Masculino\nOpção: ")
while sexo != "f" and sexo != "m":
    print("Sexo Inválido")
    sexo = input("Digite seu sexo:\nf - Feminino\nm - Masculino\nOpção: ")

# Pede o estado civil do usuário e verifica se é "s", "c", "v" ou "d"
estciv = input("Digite seu estado civil: \ns - Solteiro\nc - Casado\nv - Viúvo\nd - Divorciado\nOpção: ")
while estciv != "s" and estciv != "c" and estciv != "v" and estciv != "d":
    print("Estado Civil Inválido")
    estciv = input("Digite seu estado civil: \ns - Solteiro\nc - Casado\nv - Viúvo\nd - Divorciado\nOpção: ")

# Imprime os dados inseridos
print("Seus dados foram cadastrados com sucesso")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Salário: {salario}")
print(f"Sfexo: {sexo}")
print(f"Estado Civil: {estciv}")
