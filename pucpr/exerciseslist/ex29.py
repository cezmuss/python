# Lista de Exercícios
# Exercício 29

# Define "preco"
preco = 1.99

# Imprime nome da loja e tabela de preços
print("Lojas Quase Dois - Tabela de Preços")

for i in range(1, 51):
    print(f"{i:2} - R${preco:2}")
    preco += 1.99

"""
as linhas de código abaixo é somente um complemento ao código
onde eu pergunto para o caixa a quantidade de produtos do cliente
e o caixa já recebe o custo da compra do cliente, não precisando
procurar na tabela :))
"""

# Pede a quantidade de produtos do cliente, verifica se está entre 1 e 50 e calcula o total
while True:
    num = int(input("Digite a quantidade de produtos do cliente: "))
    if num < 1 or num > 50:
        print("Quantidade Inválida")
        continue
    else:
        # Calcula e imprime o total a ser pago
        total = num * 1.99
        print(f"O total a ser pago é de: R${total:2}")
        break
