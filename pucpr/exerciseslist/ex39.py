# Lista de Exercícios
# Exercício 39

# Listas vazias que conterão o numero de alunos e as alturas
numero_alunos = []
altura_alunos = []

# Entrada dos dados
for i in range(10):
    print(f"{i + 1}° Aluno")
    n_aluno = int(input("Digite o número do aluno: "))
    while n_aluno in numero_alunos:
        print("[Este número ja foi digitado]")
        n_aluno = int(input("Digite outro número: "))
    a_aluno = altura_alunos.append(float(input("Digite a altura do aluno: ")))
    numero_alunos.append(n_aluno)

indice_baixo = altura_alunos.index(min(altura_alunos))
indice_alto = altura_alunos.index(max(altura_alunos))

# Imprime o número do aluno mais baixo e do mais alto e suas respectivas alturas
print(f"Aluno mais baixo número: {numero_alunos[indice_baixo]}\nAltura: {min(altura_alunos)}")
print(f"Aluno mais alto número: {numero_alunos[indice_alto]}\nAltura: {max(altura_alunos)}")
