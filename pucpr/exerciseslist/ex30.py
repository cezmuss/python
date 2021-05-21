# Lista de Exercícios
# Exercício 30

# Pede o preço do pão, imprime nome da panificadora e difine "custo"
preco = float(input("Preço do Pão: R$ "))
print("Panificadora Pão de Ontem - Tabela de Preços")
custo = preco

# Calcula o custo
for i in range(1, 51):
    print(f"{i:2} - R${custo:2}")
    custo += preco

"""
as linhas de código abaixo é somente um complemento ao código
onde eu pergunto a quantidade de pães do cliente e o
caixa já recebe o custo da compra do cliente, não precisando
procurar na tabela :))
"""

# Pede a quantidade de pães, verifica se está entre 1 e 50 e calcula o total
while True:
    paes = int(input("Digite a quantidade de pães: "))
    if paes < 1 or paes > 50:
        print("Quantidade Inválida")
        continue
    else:
        # Calcula e imprime o total a ser pago
        total = paes * preco
        print("O total a ser pago é de: R${:.2f}".format(total))
        break
