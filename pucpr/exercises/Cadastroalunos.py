"""
Sistema de cadastro de alunos, exemplo abaixo

alunos = {
    '123456': {
        'nome': 'Marcos',
        'sobrenome': 'Pontes',
        'email': 'marcos@pontes.com'
    }
}
"""

#Estrutura de base do dicionário
alunos = {}

#Dados a serem solicitados
dados = [
    "matrícula",
    "nome",
    "sobrenome",
    "email"
]

while True:
    # Cadastro do aluno
    matricula = ""
    for dado in dados:
        valor = input(f"Por favor, entre com {dado}: ")
        # Montar a estrutura do dicionário
        if dado == "matrícula":
            matricula = valor
            # Cria elemento do dicionário alunos
            alunos[valor] = {}
        else:
            # Cria novo elemento no registro de aluno
            alunos[matricula][dado] = valor

    # Mensagem/condição de saída
    resp = input("Gostaria de cadastrar mais um aluno [S/N]? ").upper()
    if resp == "N":
        break

print(alunos)
