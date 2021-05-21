# Lista de Exercícios
# Exercício 37

# Cria 3 listas vazias e define "n_cliente"
cod_clientes = []
altura_clientes = []
peso_clientes = []
n_cliente = 1
codigo = True

# Condição de saída e pede as informações dos clientes
while codigo != 0:
    print("Digite '0' para finalizar")
    print(f"Cliente {n_cliente}")
    codigo = int(input("Digite o código do cliente: "))
    if codigo == 0:
        break
    else:
        altura = float(input("Digite a altura do cliente: "))
        peso = float(input("Digite o peso do cliente: "))
        cod_clientes.append(codigo)
        altura_clientes.append(altura)
        peso_clientes.append(peso)
        n_cliente += 1

# Calcula os códigos de cada característica
cod_magro = peso_clientes.index(min(peso_clientes))
cod_gordo = peso_clientes.index(max(peso_clientes))
cod_alto = altura_clientes.index(max(altura_clientes))
cod_baixo = altura_clientes.index(min(altura_clientes))

# Imprime os resultados
print("-------" * 5)
print(f"Código do mais magro: {cod_clientes[cod_magro]}")
print(f"Peso: {min(peso_clientes)}")
print(f"Código do mais gordo: {cod_clientes[cod_gordo]}")
print(f"Peso: {max(peso_clientes)}")
print(f"Código do mais alto: {cod_clientes[cod_alto]}")
print(f"Altura: {max(altura_clientes)}")
print(f"Código do mais baixo: {cod_clientes[cod_baixo]}")
print(f"Altura: {min(altura_clientes)}")
print(f"Média de altura: {sum(altura_clientes) / len(altura_clientes):2}")
print(f"Média de peso: {sum(peso_clientes) / len(peso_clientes):2}")
