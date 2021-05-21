# Lista de Exercícios
# Exercício 45

# Definição das listas
gabarito = []
respostas_aluno = []
notas_tiradas = []

print("Professor")

# Entrada de dados e condição de saída
for i in range(10):
    print(f"Questão n°{i + 1}: ")
    resposta_certa = gabarito.append(input("Digite a alternativa correta: "))
n_aluno = 1
continuar = True
while continuar != 'N':
    print(f"Aluno n°{n_aluno}: ")
    respostas_aluno.clear()
    for i in range(10):
        print(f"Questão n°{i + 1}: ")
        resposta_aluno = respostas_aluno.append(input("Escolha a alternativa: "))
    nota = 0
    for i in range(10):
        if respostas_aluno[i] == gabarito[i]:
            nota += 1
    notas_tiradas.append(nota)
    continuar = input("Outro aluno vai utilizar o sistema? [S/N] ").upper()
    n_aluno += 1

# Imprime os resultados
print(f"{len(notas_tiradas)} alunos utilizaram o sistema")
print(f"A maior nota tira foi: {max(notas_tiradas)}")
print(f"A menor nota tirada foi: {min(notas_tiradas)}")
print(f"A media de notas da turma foi de: {sum(notas_tiradas) / len(notas_tiradas)}")
print(notas_tiradas)
