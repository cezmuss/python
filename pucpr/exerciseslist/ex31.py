# Lista de Exercícios
# Exercício 31

# Imprime nome da loja e define "n" e "total"
while True:
    print("Lojas Tabajara")
    n = 1
    total = 0

    # Pede o preço do produto e calcula o total
    while True:
        preco = float(input(f"Produto {n}: R$ "))
        n += 1
        total += preco
        if preco == 0:
            break

    print("------------------------------------")

    # Imprime o total, pede um número e calcula e imprime o troco
    print(f"Total: R$ {total:2} ")
    dinheiro = float(input("Dinheiro: R$ "))
    print(f"Troco: R$ {dinheiro - total:2}")

    print("------------------------------------")

    # Condição de saída
    reset = input("Pressione 0 para reiniciar a operação, 1 para encerrar: ")
    if reset == "0":
        continue
    else:
        print("Encerrando caixa...")
        break
